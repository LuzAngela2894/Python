"""Esta clase se utiliza para interactuar con una tabla de usuarios 
en una base de datos utilizando SQLAlchemy. Los atributos de la clase 
corresponden a las columnas en la tabla. CRUD."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())

    @classmethod
    def create(cls, username):
        user = User(username=username)
        return user.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except:
            return False
    
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at
        }

    def update(self):
        self.save()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except:
            return False

    def decorator_name(function):
        def wrap(*args, **kwargs):
            return function(*args, **kwargs)

        wrap.__name__ = function.__name__
        return wrap
