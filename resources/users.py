from flask import Blueprint, jsonify, request
from models.modelUser import User
import database as db

users = Blueprint('users', __name__)

@users.route('/users')
def getUsers():
    users = User.query.order_by(User.name).all()
    return jsonify([users.to_json() for user in users])

@users.route('/users', methods=['POST'])
def postUsers():
    user = User.from_json(request.json)
    db.db_session.add(user)
    db.db_session.commit()
    return jsonify(user.to_json()), 201

#Verificar db_session (Melhorar config do banco)
#Por enquanto só linkar ele com o último user criado
#Criar login de access token