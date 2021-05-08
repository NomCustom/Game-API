from flask import Flask, jsonify, request, render_template, flash, session
from functools import wraps
import jwt
from datetime import datetime
import datetime

app = Flask("Game API")
jeux_liste = [
	{
		"id": 0,
		"type": "action",
		"creators": "InnerSloth",
		"name": "Among Us",
		"short_desc": "Jouez en ligne ou sur wi-fi local avec 4-10 joueurs que vous essayez de préparer votre vaisseau spatial pour le départ, mais méfiez-vous que l’on sera un imposteur plié sur tuer tout le monde!",
		"long_desc": "Les membres d'équipage peuvent gagner en complétant toutes les tâches ou en découvrant et en votant l'imposteur à bord du navire. L’Imposteur peut utiliser le sabotage pour provoquer le chaos, en facilitant la mort et en améliorant les alibis."
	},
	
	{
		"id": 1,
		"type": "aventure", 
		"creators": "Roblox Corporation", 
		"name": "Roblox",
		"short_desc": "Une des plus grandes plateformes au monde de jeux créés par la communauté.",
		"long_desc": "Roblox est l'univers virtuel ultime qui vous permet de jouer, de créer et d'incarner tout ce dont vous rêvez. Rejoignez des millions de joueurs et découvrez d'innombrables mondes immersifs créés par une communauté internationale ! Vous avez déjà un compte ? Connectez-vous à votre compte Roblox et jouez dès maintenant ! DES MILLIONS DE MONDES À EXPLORER \nVous avez envie de jouer à un RPG épique ? Vous rêvez d'affronter des joueurs du monde entier ? Ou vous voulez juste passer du temps avec vos amis en ligne ? Grâce à la multitude de mondes créés régulièrement par la communauté, vous aurez sans arrêt des univers à découvrir. \nJOUEZ ENSEMBLE OÙ ET QUAND VOUS VOULEZ\nJouez où vous voulez. Roblox est multi-plateformes : vous pouvez jouer avec vos amis et des millions d'autres joueurs sur ordinateur, appareil mobile, Xbox One et casque de réalité virtuelle. \nDEVENEZ QUI VOUS VOULEZ \nFaites preuve de créativité et démarquez-vous ! Personnalisez votre avatar avec des tonnes de chapeaux, t-shirts, visages, objets, etc. Grâce au catalogue d'objets qui grandit chaque jour, votre originalité n'a pas de limite.\nDISCUTEZ AVEC VOS AMIS\nPassez du temps avec des amis du monde entier grâce au chat, aux messages privés et aux groupes !"
	}
]


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
