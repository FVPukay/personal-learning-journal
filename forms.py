from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, NumberRange, Length


class EntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired(),
                    Length(max=40)]  # Keeps titles nicely centered
        )
    date = DateField(
        'Date',
        format='%Y-%m-%d',
        validators=[DataRequired()],
        render_kw={'placeholder': 'YYYY-MM-DD'}
        )
    time_spent = IntegerField(
        'Time Spent (Minutes)',
        validators=[
            DataRequired(),
            NumberRange(
                min=1,
                max=9999999999,  # Prevents OverflowError int to SQLite INTEGER
                message="Must Be Integer Between 1 And 9999999999.")
        ])
    what_you_learned = TextAreaField(
        'What you learned',
        validators=[DataRequired()]
        )
    resources_to_remember = TextAreaField(
        'Resources to remember',
        validators=[DataRequired()]
        )


class CatchaForm(FlaskForm):
    catcha_code = StringField(
        'Confirm CATCHA below',
        validators=[DataRequired()]
        )
