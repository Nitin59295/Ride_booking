from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

class Vehicles:
    __tablename__ ='vehicles'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)

class Rides:
    __tablename__ ='rides'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)


class Payments:
    __tablename__ ='payments'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

class Ratings:
    __tablename__ ='ratings'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String, nullable=False)