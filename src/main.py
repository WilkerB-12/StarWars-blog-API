"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import requests
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import Character, db, User, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET','POST'])
def handle_character():
    if request.method == 'GET':
        characters= Character.query.all()
        return jsonify(list(map(
            lambda character: character.serialize(), 
            characters))), 201
    else:
        body=request.json
        character=Character.create(
            name=body['name'],
            eye_color=body['eye_color'],
            birth_year=body['birth_year'],
            gender=body['gender']
        )
        dictionary= character.serialize()
        print(dictionary)
        return jsonify(dictionary), 201

@app.route('/planets', methods=['GET','POST'])
def handle_planet():
    if request.method == 'GET':
        planets= Planet.query.all()
        return jsonify(list(map(
            lambda planet: planet.serialize(), 
            planets))), 201
    else:
        body=request.json
        planet=Planet.create(
            name=body['name'],
            diameter=body['diameter'],
            rotation_period=body['rotation_period'],
            orbital_period=body['orbital_period']
        )
        dictionary= planet.serialize()
        print(dictionary)
        return jsonify(dictionary), 201


BASE_URL="https://www.swapi.tech/api"

@app.route('/populate-characters',methods=["POST"])
def populate_characters():
    response=requests.get(
        f"{BASE_URL}{'/people'}"
    )
    #cuerpo con todos los charracters
    body=response.json()
    all_characters=[]

    #ciclo recorrer la respuesta y obtener detalles de cada uno    
    for result in body['results']:
        response=requests.get(result['url'])
        body=response.json()

    #se agregan las propiedades de cada character a la lista
        all_characters.append(body['result']['properties'])
    instances=[]
    #recorremos la lista con todos los personajes y creamos la instancia
    for character in all_characters:
        instance=Character.create(character)
    #agregamos el OBJETO character a la lista instance
        instances.append(instance)

    return jsonify(list(map(
        lambda inst: inst.serialize(), 
        instances
    ))),200

@app.route('/populate-planets',methods=["POST"])
def populate_planets():
    response=requests.get(
        f"{BASE_URL}{'/planets'}"
    )
    #cuerpo con todos los charracters
    body=response.json()
    all_planets=[]

    #ciclo recorrer la respuesta y obtener detalles de cada uno    
    for result in body['results']:
        response=requests.get(result['url'])
        body=response.json()

    #se agregan las propiedades de cada character a la lista
        all_planets.append(body['result']['properties'])
    instances=[]
    #recorremos la lista con todos los personajes y creamos la instancia
    for planet in all_planets:
        instance=Planet.create(planet)
    #agregamos el OBJETO character a la lista instance
        instances.append(instance)

    return jsonify(list(map(
        lambda inst: inst.serialize(), 
        instances
    ))),200

@app.route('/populate-vehicles',methods=["POST"])
def populate_vehicles():
    response=requests.get(
        f"{BASE_URL}{'/vehicles'}"
    )
    #cuerpo con todos los charracters
    body=response.json()
    all_vehicles=[]

    #ciclo recorrer la respuesta y obtener detalles de cada uno    
    for result in body['results']:
        response=requests.get(result['url'])
        body=response.json()

    #se agregan las propiedades de cada character a la lista
        all_vehicles.append(body['result']['properties'])
    instances=[]
    #recorremos la lista con todos los personajes y creamos la instancia
    for vehicle in all_vehicles:
        instance=Vehicle.create(vehicle)
    #agregamos el OBJETO character a la lista instance
        instances.append(instance)

    return jsonify(list(map(
        lambda inst: inst.serialize(), 
        instances
    ))),200
@app.route('/characters/<int:character_id>')
def single_member(character_id):
    character=Character.query.get(character_id)
    return jsonify(character.serialize()),200

@app.route('/planets/<int:planet_id>')
def single_planet(planet_id):
    planet=Planet.query.get(planet_id)
    return jsonify(planet.serialize()),200

@app.route('/vehicles/<int:vehicle_id>')
def single_vehicle(vehicle_id):
    vehicle=Vehicle.query.get(vehicle_id)
    return jsonify(vehicle.serialize()),200


@app.route('/characters/<int:id>',methods=['DELETE'])
def delete_members(id):
    character = Character.query.get(id)
    character.delete()
    return jsonify({"done":True}),200

    
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5432))
    app.run(host='0.0.0.0', port=PORT, debug=False)
