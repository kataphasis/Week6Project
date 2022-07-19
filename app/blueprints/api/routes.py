from flask import jsonify, request, redirect, flash
from . import bp as app
from app.blueprints.main.models import Pokemon
from flask_login import current_user
from app import db

@app.route("/users")
def users():
    user_dict = {
        
    }

    return jsonify(user_dict)



    