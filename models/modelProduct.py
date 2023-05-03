from database import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    quantity = db.Column(db.Integer, nullable=True)

    id_list = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=False)
    list = db.relationship('List')
    
    def __init__(self, name=None, quantity=None):
        self.name = name
        self.quantity = quantity
    
    def to_json(self):
        json_products = {
            'name': self.name,
            'quantity': self.quantity
        }
        return json_products

    @staticmethod
    def from_json(json_products):
        name = json_products.get('name')
        quantity = json_products.get('quantity')
        return Product(name=name, quantity=quantity)