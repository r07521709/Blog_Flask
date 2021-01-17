# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
# To create the initial database, just import the db object from an interactive Python shell
# The next steps are in the above URL
from datetime import datetime
from flask import current_app
from flask_login import UserMixin
import jwt
from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref=db.backref('author', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username

    # https://github.com/jpadilla/pyjwt
    def generate_reset_password_token(self):
        return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def check_reset_password_token(token):
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            return User.query.filter_by(id=data['id']).first()
        except:
            return
            
class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        body = db.Column(db.String(140), nullable=False)
        timestamp = db.Column(db.DateTime, default=datetime.utcnow)
        # If there is no modification in Flask, the table name will be lowercase of the class name. So it would be 'user.id'.
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        def __repr__(self):
            return '<Post {}>'.format(self.body)



