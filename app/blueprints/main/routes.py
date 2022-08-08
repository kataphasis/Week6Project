from flask import render_template, redirect, url_for, request, flash
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import login_required, current_user
import requests
from app import db

my_request = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = my_request.json()

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

@app.route("/addpokemon", methods=['GET', 'POST'])
def addpokemon():
    if request.method == "POST":
        check_pokemon = Pokemon.query.filter_by(name=request.form['inputName']).first()
        if check_pokemon is not None:
            flash('This pokemon is already in the database!')
        else:
            if request.form['inputName'] == request.form['inputNameConfirm']
                new_pokemon = Pokemon(
                    id=json_data['id'],
                    name=json_data['name'],
                    type=json_data['types'][0]['type']['name'],
                    ability1=json_data['abilities'][0]['ability']['name'],
                    ability2=json_data['abilities'][1]['ability']['name'],
                    statName1=json_data['stats'][0]['stat']['name'],
                    statValue1=json_data['stats'][0]['base_stat'],
                    statName2=json_data['stats'][1]['stat']['name'],
                    statValue2=json_data['stats'][1]['base_stat'],
                    statName3=json_data['stats'][2]['stat']['name'],
                    statValue3=json_data['stats'][2]['base_stat'],
                    weight=json_data['weight'],
                    sprite=json_data['sprites']['front_default']
                )
                db.session.add(new_pokemon)
                db.session.commit()
    return render_template("/addpokemon.html")

@app.route("/usercollection")
def usercollection():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('usercollection.html')