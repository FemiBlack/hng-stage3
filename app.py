from form import ContactForm
from flask import Flask, render_template, request, url_for
from form import ContactForm
from flask_mail import Mail
from utils import send_mail

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587 #465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

@app.route("/", methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        user=form
        send_email(user)
        flash(f'Hey {user.name}, Your email has been recieved successfully.', 'info')
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)