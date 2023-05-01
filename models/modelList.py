import sqlalchemy as db
from database import Base
from models.modelUser import User

class List(Base):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column("user_id", db.ForeignKey(User.id))
    def to_json(self):
        json_lists = {
            'id': self.id,
        }
        return json_lists

    @staticmethod
    def from_json(json_lists):
        id = json_lists.get('id')
        return List(id=id)