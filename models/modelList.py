from database import db

class List(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)

    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User')

    def to_json(self):
        json_lists = {
            'id': self.id,
        }
        return json_lists

    @staticmethod
    def from_json(json_lists):
        id = json_lists.get('id')
        return List(id=id)