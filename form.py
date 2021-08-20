from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):

    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
