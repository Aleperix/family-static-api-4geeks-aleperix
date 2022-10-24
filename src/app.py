"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Obtenemos todos los miembros de la familia en formato Json
@app.route('/members', methods=['GET'])
def handle_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    return jsonify(members), 200

#Obtenemos un miembro de la familia en formato Json a través de su ID
@app.route('/member/<int:member_id>', methods=['GET'])
def handle_one_member(member_id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)

    if member == True:
        return jsonify(member), 200
    else:
        return "La ID ingresada no existe", 404

#Agregamos un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def handle_add_member():

    # this is how you can use the Family datastructure by calling its methods
    body = json.loads(request.data)
    member = jackson_family.add_member(body)

    if member == True:
        return "Miembro "+body["first_name"]+" agregado con éxito", 200
    else:
        return "Debes ingresar todas las propiedades con su respectivo valor", 400

#Eliminamos un miembro de la familia a través de su ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.delete_member(member_id)
    
    if member == "last":
        return "No puedes eliminar el único miembro de la familia", 400
    if member == True:
        return "Miembro eliminado con éxito", 200
    else:
        return "La ID ingresada no existe", 404

#Actualizamos un miembro de la familia a través de su ID
@app.route('/member/<int:member_id>', methods=['PUT'])
def handle_update_member(member_id):

    # this is how you can use the Family datastructure by calling its methods
    body = json.loads(request.data)
    member = jackson_family.update_member(member_id, body)

    if member == True:
        return "Miembro modificado con éxito", 200
    else:
        return "La ID ingresada no existe", 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
