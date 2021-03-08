from flask import Flask, jsonify, json

app = Flask(__name__)

data_pokemons = json.load(open("Database/pokedex.json", encoding="utf8"))
data_types = json.load(open("Database/types.json", encoding="utf8"))


@app.route('/')
def index():
    return "Welcome to a simple pokemon api - Andrei-Eduard Constantinescu"


@app.route('/pokemons/', methods=['GET'])
def get_pokemons():
    return jsonify({'Pokemons': data_pokemons})


@app.route('/pokemons/<int:id>', methods=['GET'])
def get_pokemon_by_id(id):
    try:
        return jsonify({'Pokemon': data_pokemons[id]})
    except IndexError:
        return "No such pokemon with that id"


@app.route('/pokemons/<string:name>', methods=['GET'])
def get_pokemon_by_name(name):

    for pokemon in data_pokemons:
        if name in pokemon['name'].values():
            return jsonify({'Pokemon': pokemon})

    return "No pokemon with that name!"


@app.route('/types/', methods=['GET'])
def get_types():
    return jsonify({'Types': data_types})


@app.route('/types/<string:type>/', methods=['GET'])
def get_pokemons_by_types(type):
    pokemon_by_types = []
    for pokemon in data_pokemons:
        if type in pokemon['type']:
            pokemon_by_types.append(pokemon)

    return jsonify({'Pokemons': pokemon_by_types})


@app.route('/pokemons/sorted/<string:prop>/', methods=['GET'])
def get_pokemons_sorted(prop):

    if prop == "SpAttack":
        prop = "Sp. Attack"

    if prop == "SpDefense":
        prop = "Sp. Defense"

    pokemons = []
    for pokemon in data_pokemons:
        pokemons.append(pokemon)

    try:
        pokemons.sort(key=lambda p: p['base'][prop])
        return jsonify({'Pokemons': pokemons})
    except KeyError:
        return "Property not found in pokedex!"


@app.route('/pokemons/sorted/<string:prop>/Reversed/', methods=['GET'])
def get_pokemons_sorted_reversed(prop):

    if prop == "SpAttack":
        prop = "Sp. Attack"

    if prop == "SpDefense":
        prop = "Sp. Defense"

    pokemons = []
    for pokemon in data_pokemons:
        pokemons.append(pokemon)

    try:
        pokemons.sort(key=lambda p: p['base'][prop], reverse=True)
        return jsonify({'Pokemons': pokemons})
    except KeyError:
        return "Property not found in pokedex!"


@app.errorhandler(404)
def page_not_found(a):
    return "Page not found!"


if __name__ == "__main__":
    app.run()
