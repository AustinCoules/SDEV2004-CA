# Author: Austin Coules (C23444946)
# Author: Oscar Canavan (C24425236)
# Author: Daniel Courage (C23491584)

from flask import Flask, request, session
from flask_babel import Babel

def get_locale():
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(['en', 'de', 'pl']) or 'en' # Fallback

app = Flask(__name__)

app.secret_key='asecretkey'

babel = Babel(app, locale_selector=get_locale)

from app import routes