from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired, Length
from models import db, Users


class UsersForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    designation = StringField('Designation', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Submit')