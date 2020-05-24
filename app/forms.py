from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class AddRssUrl(FlaskForm):
    rssUrl = StringField('RSS URL', validators=[DataRequired()])
    submit = SubmitField('Add URL into DB')

class AddUser(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add Email into DB')