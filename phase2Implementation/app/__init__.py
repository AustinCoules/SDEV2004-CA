from flask import Flask, session
from flask_babel import Babel

def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(['en', 'de', 'pl'])

app = Flask(__name__)

app.secret_key='asecretkey' # TODO: change this to a secure key in production

babel = Babel(app)

babel.init_app(app, locale_selector=get_locale)

from app import routes