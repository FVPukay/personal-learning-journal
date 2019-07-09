from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, NumberRange


class EntryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time_spent = IntegerField('Time Spent', validators=[DataRequired(), NumberRange(min=1)])
    what_you_learned = TextAreaField(
        'What you learned', validators=[DataRequired()]
    )
    resources_to_remember = TextAreaField(
        'Resources to remember', validators=[DataRequired()]
    )
