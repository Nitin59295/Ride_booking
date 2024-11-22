from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from models import db, Users, Vehicles, Rides, Ratings, Payments
from forms import UsersForm, VehicleForm

main = Blueprint('main', __name__)

@main.route('/')
def homes():
    user = Users.query.all()
    return render_template('home.html', user=user)

@main.route('/login', methods=['GET', 'POST'])
def login():
    user = Users.query.all()
    return render_template('login.html', user=user)

@main.route('/new/user', methods=['GET', 'POST'])
def add_user():
    form = UsersForm()
    if form.validate_on_submit():
        existing_user = Users.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('This email already exists')
            return render_template('add_user.html', form=form)

        new_user = Users(
            name=form.name.data,
            email=form.email.data,  
            password=form.password.data 
        )
      
        db.session.add(new_user)
        db.session.commit()

       
        return redirect(url_for('main.homes'))
  
    return render_template('add_user.html', form=form)


@main.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    form = VehicleForm()
    if form.validate_on_submit():
        new_vehicle = Vehicles(name=form.name.data, model=form.model.data)

        db.session.add(new_vehicle)
        db.session.commit()

        return redirect(url_for('main.list_vehicles'))

    return render_template('add_vehicle.html', form=form)

@main.route('/list_vehicles')
def list_vehicles():
    vehicles = Vehicles.query.all()
    return render_template('list_vehicles.html', vehicles=vehicles)


