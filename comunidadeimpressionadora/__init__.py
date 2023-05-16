from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy
from sqlalchemy import inspect, Inspector, inspection

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:BvKCN0reD0AVyg89rf2f@containers-us-west-16.railway.app:5488/railway'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Faça o Login ou cadastre-se para acessar o conteúdo'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import models

engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not sqlalchemy.engine.reflection.Inspector.has_table(inspection, "usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('base de dados criada')
else:
    print('Base já está criada')

from comunidadeimpressionadora import routes
