from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:пароль@localhost:5432/имя базы'
app.config['SQLAlchemy_TRACK_MODIFIVATTION'] = False
