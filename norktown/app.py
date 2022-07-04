from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from citizen.ControllerCitizen import ControllerCitizen
from vehicle.ControllerVehicle import ControllerVehicle

# Inicializar objeto central app do Flask.
app = Flask(__name__)

# Incializar objeto central db do SQLAlchemy.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://solda_db_user:solda_db_password@db:5432/solda_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição de rotas.
@app.route('/')
def hello_world():
    return 'Home'

# Rota do Citizen.
@app.route('/citizen', methods=['GET', 'POST'])
def inicialize_citizen():
    return getRequestFromController(ControllerCitizen())

# Rota do Vehicle
@app.route('/vehicle', methods=['GET', 'POST'])
def inicialize_vehicle():
    return getRequestFromController(ControllerVehicle())    

# Retorna a requisição de acordo com o Controller fornecido como parâmetro.
# Post -> adicionar registro.
# Get -> consultar registro.
def getRequestFromController(controller):
    if request.method == 'POST':        
        return controller.post(request.form)
    return controller.get(request.args)

# Definir debug, endereço e porta.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
    )