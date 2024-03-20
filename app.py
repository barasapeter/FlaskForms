import os
from datetime import datetime

from flask import Flask
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

from flask import render_template, session, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'suck my balls'

moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=["POST", 'GET'])
def main():
	from forms import NameForm
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('It looks like you have changed your name!')
		session['name'] = form.name.data
		return redirect(url_for('main'))
	return render_template('main.html', form=form, name=session.get('name'))


@app.route('/b')
def home():
	return session.get('name', 'huh?')
	
if __name__ == '__main__':
	for directory in 'static', 'templates':
		if not os.path.exists(directory):
			os.mkdir(directory)
			
	app.run(debug=True)	
