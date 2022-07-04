from flask import jsonify
from citizen.ModelCitizen import ModelCitizen
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Controller do Citizen.
class ControllerCitizen():

    # Constructor
    def __init__(self):
        self.ModelCitizen = ModelCitizen()

    # Método 'GET'.
    def get(self, args):
        try:
            if len(args) == 0:
                return jsonify(ModelCitizen.serialize_list(self.ModelCitizen.query.all()))
            if 'cpf' in args:
                return jsonify(self.ModelCitizen.query.filter_by(ctzcpf = args['cpf']).one().get_dictionary_format())
            if 'id' in args:
                return jsonify(self.ModelCitizen.query.filter_by(ctzid = args['id']).one().get_dictionary_format())
        except:
            return jsonify([])

    # Método 'POST'.
    def post(self, args):
        self.ModelCitizen.ctzname = args["name"]
        self.ModelCitizen.ctzcpf = args["cpf"]
        if "address" in args:
            self.ModelCitizen.ctzaddress = args["address"]
        db.session.add(self.ModelCitizen)
        db.session.commit()
        return jsonify(self.ModelCitizen.get_dictionary_format())