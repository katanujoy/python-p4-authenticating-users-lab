#!/usr/bin/env python3

from flask import Flask, session
from flask_migrate import Migrate
from flask_restful import Api

from models import db, User
from resources import Login, Logout, CheckSession

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# Register resources
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')

if __name__ == '__main__':
    app.run(port=5555)
