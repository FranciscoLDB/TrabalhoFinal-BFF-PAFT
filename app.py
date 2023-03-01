from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
apiKey = 'a52d564a84702ae0175b97bb00f173af';

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

@app.route('/searchfilme')
def searchfilme():
    filme = request.args.get('filme')
    urlSearch = 'https://api.themoviedb.org/3/search/movie?api_key=a52d564a84702ae0175b97bb00f173af&query=' + filme

    respSearch = requests.get(urlSearch)
    jsonSearch = respSearch.json()
    urlImg = jsonSearch.get('results')[0].get('poster_path')
    resp = {
        'titulo': jsonSearch.get('results')[0].get('original_title'),
        'data': jsonSearch.get('results')[0].get('release_date'),
        'foto': 'https://image.tmdb.org/t/p/w500' + urlImg,
        'nota': jsonSearch.get('results')[0].get('vote_average'),
    }
    return resp

app.run(debug=True)