# https://github.com/alphafan/flask-user-auth-example/blob/master/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):


    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'
    # Recaptcha key (test key form https://developers.google.com/recaptcha/docs/faq)
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Gmail Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    # Instead of setting MAIL_USERNAME & MAIL_PASSWORD here(config.py), using environmental variables to set could avoid direct exposure.
    # And enable permissions on https://www.google.com/settings/security/lesssecureapps.
    # Reference: https://github.com/twtrubiks/Flask-Mail-example
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'r07521709@g.ntu.edu.tw'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Young5078'