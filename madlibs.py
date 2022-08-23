"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    user_choice = request.args.get('game')

    if user_choice == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    input_person = request.args.get("madlib-person")
    input_color = request.args.get("madlib-colors")
    input_noun = request.args.get("madlib-noun")
    input_adj = request.args.get("madlib-adjective")

    return render_template("madlib.html", person=input_person, color=input_color, noun=input_noun, adjective=input_adj)


    #return render_template("madlib.html", person_choice=input_person, color_choice=input_color, noun_choice=input_noun, adj_choice=input_adj)

# @app.route("/goodbye")
# def say_goodbye():
#     return render_template("goodbye.html")


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
