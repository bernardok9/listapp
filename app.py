from flask import Flask
from config import config
from database import db
from models.modelList import List
from models.modelProduct import Product
from models.modelUser import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

User
Product
List

@app.route('/db')
def datab():
    db.create_all()
    return '<h2> init database </h2>'