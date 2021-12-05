from flask import Flask, render_template, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the secret bird.app string'  # secret key for WTF to protect form communication

bootstrap = Bootstrap(app)
moment = Moment(app)

class BirdForm(FlaskForm):
    birdname = StringField('Provide Bird Name', validators=[DataRequired()])
    submit = SubmitField('Search')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/", methods=['GET', 'POST'])
def index():
    form = BirdForm()
    if form.validate_on_submit():
        session['birdname'] = form.birdname.data
        if session.get('birdname').strip() == "oli":
            flash('hi oli, you are not a bird!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, birdname=session.get('birdname'), current_time=datetime.utcnow(), locale='es')

@app.route("/bird/<name>")
def bird(name):
    return render_template('user.html', name=name)

@app.route("/wiki")
def wiki():
    return redirect('http://wikipedia.org')

if __name__ == "__main__":
    app.run()
