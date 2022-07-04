from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Modelo de Citizen.
class ModelCitizen(db.Model):

    # Definição de campos
    __tablename__ = 'tbcitizen'
    ctzid = db.Column(db.Integer, primary_key = True)
    ctzname = db.Column(db.String(20), nullable = False)
    ctzcpf = db.Column(db.String(11), nullable = False)
    ctzaddress = db.Column(db.String(100), nullable = True)

    # Serializa lista com registros do modelo.
    @staticmethod    
    def serialize_list(unserialized_citizens_list):
        serialized_citizens_list = []
        for ModelCitizen in unserialized_citizens_list:
            serialized_citizens_list.append(ModelCitizen.get_dictionary_format())
        return serialized_citizens_list

    # Retorna atributos no formato Dictionary
    def get_dictionary_format(self):
        return {"ID"      : self.ctzid,
                "Name"    : self.ctzname,
                "Cpf"     : self.ctzcpf,
                "Address" : self.ctzaddress}    