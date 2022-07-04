from flask import jsonify, Response
from citizen.ModelCitizen import ModelCitizen
from vehicle.ModelVehicle import ModelVehicle
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Controller de Vehicle.
class ControllerVehicle:

    # Constructor
    def __init__(self):
        self.ModelVehicle = ModelVehicle()
        self.ModelCitizen = ModelCitizen()

    # Método 'GET'.
    def get(self, args):
        try:
            if len(args) == 0:
                return jsonify(ModelVehicle.serialize_list(self.ModelVehicle.query.all()))
            if 'id' in args:
                return jsonify(self.ModelVehicle.query.filter_by(vclid = args['id']).one().get_dictionary_format())
            if 'plate' in args:
                return jsonify(self.ModelVehicle.query.filter_by(vclplate = args['plate']).one().get_dictionary_format())
            if 'cpf' in args:
                return jsonify(ModelVehicle.serialize_list(self.ModelVehicle.query.join(ModelCitizen).filter_by(ctzcpf = args['cpf']).all()))            
        except:
            return jsonify([])

    # Método 'POST'
    def post(self, args):
        sCpf = self.getModelCitizenIdFromCpf(args["cpf"])        
        if not sCpf:
            return Response("CPF not found.", 400)
        self.ModelVehicle.vclplate = args["plate"]
        self.ModelVehicle.vclmodel = args["model"]
        self.ModelVehicle.vclcolor = args["color"]        
        self.ModelVehicle.ctzid    = sCpf
        db.session.add(self.ModelVehicle)
        db.session.commit()
        return jsonify(self.ModelVehicle.get_dictionary_format())
    
    # Retorna ID de Citizen a partir de seu CPF.
    def getModelCitizenIdFromCpf(self, cpf):
        try:
            oModelCitizen = self.ModelCitizen.query.filter_by(ctzcpf = cpf).one().get_dictionary_format()
        except:
            return False
        return oModelCitizen["ID"]
