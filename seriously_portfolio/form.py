from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from seriously_portfolio.models import Client

class ContactForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email:', validators=[DataRequired(),Email()])

    message = TextAreaField('Message:', validators=[DataRequired(), Length(min=10, max=300)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        client = Client.query.filter_by(name=name.data).first() 
        if client:
            raise ValidationError('That name is already submitted!')

    def validate_email(self, email):
        client = Client.query.filter_by(email=email.data).first() 
        if client:
            raise ValidationError('That email is already submitted!')