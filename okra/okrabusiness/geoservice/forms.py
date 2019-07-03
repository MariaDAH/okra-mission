from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from okra.models import Ecobusiness
from okra.models import Category


class SearchForm(FlaskForm):
    identifier = StringField('Identifier', validators=[DataRequired(), Length(min=2, max=100)])
    category_id = StringField('Category', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=8)])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    submit = SubmitField('Search')

    

    