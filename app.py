from flask import Flask, jsonify
from database import init_db
from models.modelProduct import Product
from database import db_session

app = Flask(__name__)

@app.route('/')
def raiz():
    return '<h2> hello world </h2>'

@app.route('/db')
def db():
    init_db()
    return '<h2> init database </h2>'

@app.route('/insert')
def insert():
    p = Product('queijo', '400')
    db_session.add(p)
    db_session.commit()
    return 'added'

@app.route('/query')
def query():
    products = Product.query.all()
    return jsonify([product.to_json() for product in products])

if __name__ == '__main__':
    app.run(debug=True)