from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired, Length
from models import db, Users


class UsersForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Length(max=100)])
    password = StringField('Password', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Add User')

class VehicleForm(FlaskForm):
    name = StringField('Vehicle Name', validators=[DataRequired(), Length(max=100)])
    model = StringField('Vehicle Model', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Add Vehicle')



# class RideForm(FlaskForm):
#     name