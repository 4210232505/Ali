from flask import Flask
from flask_sqlalchemy import SQLAlchemy

 
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/faradars'
db = SQLAlchemy(app)

import proje.models
import proje.views

