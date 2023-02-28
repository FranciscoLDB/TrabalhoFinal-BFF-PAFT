from flask import Flask, request
import requests

app = Flask(__name__)

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