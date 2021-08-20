from flask import Flask, render_template, request


app = Flask(__name__)


if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    send_reset_email(user)
    flash('An email has been sent with instructions to reset your password.', 'info')
    return redirect(url_for('users.login'))

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()