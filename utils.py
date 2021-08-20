from flask_mail import Message

def send_mail(user):
    msg = Message('Portfolio Contact', sender=user.email, recipients=[user.email, 'tadefemi02@gmail.com'])
    msg.body = user.message
    mail.send(msg)