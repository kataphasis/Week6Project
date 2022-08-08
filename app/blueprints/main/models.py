from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250))
    pokemon = db.relationship('Pokemon', backref="user", lazy="dynamic")

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)

    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    type = db.Column(db.String(20))
    ability1 = db.Column(db.String(20))
    ability2 = db.Column(db.String(20))
    statName1 = db.Column(db.String(20))
    statValue1 = db.Column(db.Integer)
    statName2 = db.Column(db.String(20))
    statValue2 = db.Column(db.Integer)
    statName3 = db.Column(db.String(20))
    statValue3 = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_user(self):
        return User.query.get(self.user_id)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)