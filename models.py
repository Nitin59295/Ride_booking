from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Vehicles(db.Model):
    __tablename__ ='vehicles'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)

class Rides(db.Model):
    __tablename__ ='rides'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)


class Payments(db.Model):
    __tablename__ ='payments'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)

class Ratings(db.Model):
    __tablename__ ='ratings'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String, nullable=False)