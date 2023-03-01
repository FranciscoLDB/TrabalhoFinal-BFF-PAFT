from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/github')
def github():
    usuario = request.args.get('usuario')
    respGit = requests.get('https://api.github.com/users/' + usuario)
    jsonGit = respGit.json()

    resp = {
        'nome': jsonGit.get('name'),
        'usuario': jsonGit.get('login'),
        'bio': jsonGit.get('bio'),
        'local': jsonGit.get('location'),
        'foto': jsonGit.get('avatar_url'),
    }
    return resp

@app.route('/pokemon')
def pokemon():
    name = request.args.get('name')

    reskPoke = requests.get('https://pokeapi.co/api/v2/pokemon/' + name)
    jsonPoke = reskPoke.json()

    respItunes = requests.get(
        'https://itunes.apple.com/search', 
        params = {"term": name,"limit": 1,"entity": "movie"}
    )
    jsonMovie = respItunes.json()
    
    resp = {
        'Pokemon': name,
        'type': jsonPoke['types'][0].get('type').get('name'),
        'movie': jsonMovie['results'][0].get('trackName')
        }
    return resp


app.run(debug=True)