"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
INSULTS = [
    'greedy', 'lazy', 'boring', 'ugly', 'dumb', 'idiot', 'jerk',
    'creepy']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <h1>Hi! This is the home page.</h1>
      <a href="http://localhost:5000/hello">Hi there!</a><br>
      <a href="http://localhost:5000/meh">Meh</a>
    </html>"""

@app.route('/meh')
def say_meh():
    """Say hi and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Oh you again...</title>
      </head>
      <body>
        <h1>Oh you again...</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def say_diss():
    """Dishes out one of several insults."""

    player = request.args.get("person")

    diss = choice(INSULTS)

    return """
     <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    compliments = ""
    for word in AWESOMENESS:
        compliments += '<option value="{}">{}</option>'.format(word, word)

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Choose your own compliment: <select name="compliment">
            {}
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(compliments)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
