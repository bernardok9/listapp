from flask import Flask, jsonify
from models.modelProduct import Product
import database as db

app = Flask(__name__)

@app.route('/')
def raiz():
    return '<h2> hello world </h2>'

@app.route('/db')
def datab():
    db.init_db()
    return '<h2> init database </h2>'

@app.route('/insert')
def insert():
    p = Product('queijo', '400')
    db.db_session.add(p)
    db.db_session.commit()
    return 'added'

@app.route('/query')
def query():
    products = Product.query.all()
    return jsonify([product.to_json() for product in products])

if __name__ == '__main__':
    app.run(debug=True)