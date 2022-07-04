from flask_sqlalchemy import SQLAlchemy
from citizen.ModelCitizen import ModelCitizen
db = SQLAlchemy()

# Modelo de Vehicle.
class ModelVehicle(db.Model):

    # Enumerados
    _enum_model = {1:"Hatch", 2:"Sedan", 3:"Convertible"}
    _enum_color = {1:"Yellow", 2:"Blue", 3:"Gray"}

    # Definição de campos
    __tablename__ = 'tbvehicle'
    vclid = db.Column(db.Integer, primary_key = True)
    ctzid = db.Column(db.Integer, db.ForeignKey(ModelCitizen.ctzid), nullable = False)
    vclplate = db.Column(db.String(7), nullable = False)
    vclmodel = db.Column(db.Integer, nullable = False)
    vclcolor = db.Column(db.Integer, nullable = False)

    # Serializa lista com registros do modelo. 
    # Utilizado para transformar informações do modelo em JSON.
    @staticmethod
    def serialize_list(unserialized_vehicles_list):
        serialized_vehicles_list = []
        for ModelVehicle in unserialized_vehicles_list:
            serialized_vehicles_list.append(ModelVehicle.get_dictionary_format())
        return serialized_vehicles_list

    # Retorna atributos no formato Dictionary.
    def get_dictionary_format(self):
        return {"ID"        : self.vclid,
                "CitizenID" : self.ctzid,
                "Plate"     : self.vclplate,
                "Model"     : self._enum_model[self.vclmodel],
                "Color"     : self._enum_color[self.vclcolor]}    