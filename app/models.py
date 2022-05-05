from app import db
from flask_login import UserMixin
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    trainer_since = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f'<User: {self.username} | {self.id} >'    

    def __str__(self):
        return f'<User: {self.username} | {self.first_name} {self.last_name}>'

    def hash_password(self, orinigal_password):
        return generate_password_hash(orinigal_password)

    def check_hash_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.username = data['username']
        self.password = self.hash_password(data['password'])

    def save(self):
        db.session.add(self)
        db.session.commit()

    
    