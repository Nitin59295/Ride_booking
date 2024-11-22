from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import db, Users, Vehicles, Rides, Ratings, Payments
from forms import UsersForm

main = Blueprint('main', __name__)

@main.route('/')
def homes():
    user = Users.query.all()
    return render_template('home.html', user=user)


@main.route('/login', methods = ['GET', 'POST'])
def login():
    user = Users.query.all() 
    return render_template('login.html', user=user)
    
@main.route('/new/user', methods=['GET', 'POST'])
def add_user():
    form = UsersForm()
    if form.validate_on_submit():
        try:
            # Create a new user instance
            new_user = Users(name=form.name.data, designation=form.designation.data)
            
            # Add the user to the database
            db.session.add(new_user)
            db.session.commit()
            
            # Redirect to home after successful submission
            return redirect(url_for('main.home'))
        except Exception as e:
            # Rollback in case of an error
            db.session.rollback()
            print(f"Error: {e}")
    
    # Render the form in the login.html template
    return render_template('login.html', form=form)

