from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(dbString, unique=True)

    def __init__(self, nome, username, password, email):
        self.nome = nome
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username


class Resultado(db.Model):
    __tablename__ = "resultados"

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.Text)

    user = db.relationship('User', foreign_keys=userId)
