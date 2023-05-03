from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)

    def __init__(self, name=None):
        self.name = name
    
    def to_json(self):
        json_users = {
            'name': self.name,
        }
        return json_users

    @staticmethod
    def from_json(json_users):
        name = json_users.get('name')
        return User(name=name)

    def __repr__(self):
        return f'<User {self.name}>'