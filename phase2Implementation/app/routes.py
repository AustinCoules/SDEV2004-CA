from app import app
from flask import render_template, session, redirect, request

@app.route('/')
@app.route('/index')
def index():
    return (render_template("index.html"))
# TODO make index file and route for it, and make it the default page when the user visits the site

# put other routes here
#
#
#
#
@app.route('/setlang/<lang_code>')
def set_language(lang_code):
# If the language mataches one of the languages we are facilitating
# Change the value of the language variable in session to that
    if lang_code in ['en', 'de', 'pl']:
        session['language'] = lang_code
# Redirect the page to the page from which the language change
# request was made
    return redirect(request.referrer or '/')

# Before each request to the app, check if the language variable
# in session has a value. If not set it to English.
@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'en' # Set default language here
