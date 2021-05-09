from flask import Flask, jsonify, request, render_template, flash, session
from functools import wraps
import jwt
from datetime import datetime
import datetime
import os
import json

fetch_path = os.getcwd()
path = fetch_path.replace("\\", "/")

app = Flask("Game API")

with open(path + '/games.json') as data:
    jeux_liste = json.load(data)

@app.route("/")
def api_home():
	return render_template('index.html')
	



@app.route("/api/games/all", methods=['GET'])
def all_games():
	return jsonify(jeux_liste)

@app.route("/api/games/<int:id>", methods=['GET'])
def get_game_by_id(id):
	for jeux in jeux_liste:
		if jeux['id'] == id:
			return jsonify(jeux)
		pass
			
@app.route("/api/games/<int:id>/type", methods=["GET"])
def get_type_of_game(id):
	for jeux in jeux_liste:
		if jeux['id'] == id:
			return jsonify(jeux['type'])
		pass

@app.route("/api/games/<int:id>/creators", methods=['GET'])
def get_creators_of_game(id):
	for jeux in jeux_liste:
		if jeux['id'] == id:
			return jsonify(jeux['creators'])
		pass

@app.route("/api/games/<int:id>/name", methods=['GET'])
def get_name_of_game(id):
	for jeux in jeux_liste:
		if jeux['id'] == id:
			return jsonify(jeux['name'])
		pass

@app.route("/api/games/<int:id>/short_desc", methods=['GET'])
def get_short_description(id):
	for jeux in jeux_liste:
		if jeux['id'] == id:
			return jsonify(jeux['short_desc'])
		pass

@app.route("/api/games/<int:id>/long_desc", methods=['GET'])
def get_long_description(id):
	for jeux in jeux_liste:
		if jeux['id'] == id:
			return jsonify(jeux['long_desc'])
		pass

if __name__ == "__main__":
	app.run(debug=True)
