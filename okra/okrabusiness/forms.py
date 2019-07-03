from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError, URL
from okra.models import Ecobusiness

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    user_id = StringField('User Id', validators=[DataRequired(), Length(min=1, max=20)])
    website = StringField('Website', validators=[DataRequired(), Length(min=2, max=100)])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=100)])
    category_id = StringField('Category', validators=[DataRequired(), Length(min=1, max=100)])
    phonenumber = StringField('Phone number', validators=[DataRequired(), Length(min=2, max=100)])
    comment = StringField('Comment', validators=[DataRequired(), Length(min=2, max=100)])
    subscriptionplan = StringField('Subscription Plan', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email'), Length(min=6, max=100)])
    #registered_on = DateTimeField( format="%Y-%m-%d %H:%M")
    #updated_on = DateTimeField(format="%Y-%m-%d %H:%M")
    submit = SubmitField('Register')

    def validate_email(self, email):
        business = Ecobusiness.query.filter_by(email=email.data).first()
        if business is not None:
            raise ValidationError('Please use a different business email.')
            
    def validate_name(self, name):
        name = Ecobusiness.query.filter_by(name=name.data).first()
        if name is not None:
            raise ValidationError('Please use a different business name.') 

    def validate_url(self, website):
        website = Ecobusiness.query.filter_by(website=website.data).first()
        if website is not None:
            raise ValidationError('This website is already registered.') 

