from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
	name = StringField(label='What is your name?', validators=[DataRequired()])
	#files = MultipleFileField('Select files')
	submit = SubmitField(label='Submit')
	