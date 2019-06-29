from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from okra.models import Business


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    userid = StringField('Userid', validators=[DataRequired(), Length(min=2, max=100)])
    website = StringField('Website', validators=[DataRequired(), Length(min=2, max=100)])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=100)])
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=100)])
    telephonenumber = StringField('Telephonenumber', validators=[DataRequired(), Length(min=2, max=100)])
    comment = StringField('Comment', validators=[DataRequired(), Length(min=2, max=100)])
    subscriptionplan = StringField('Subscriptionplan', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=100)])
    submit = SubmitField('Register')

    def validate_email(self, email):
        business = Business.query.filter_by(email=email.data).first()
        if business is not None:
            raise ValidationError('Please use a different business name.')