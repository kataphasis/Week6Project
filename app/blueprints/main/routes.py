from flask import render_template, redirect, url_for
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import login_required, current_user

@app.route("/")

def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    pokemon = Pokemon.query.all()

    pokemon.sort(key=lambda post: post.date_created, reverse=True)

    print(pokemon)

    context = {
        "pokemon": pokemon,
    }

    return render_template('index.html', **context)


@app.route("/usercollection")
def usercollection():
    return render_template('usercollection.html')