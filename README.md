# Luiz Soldatelli - Advice Health

### Descrição do projeto:

Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

### Desenvolvimento:
  
  Para atender a descrição acima, foi preparado o ambiente Docker para desenvolvimento em Python usando Flask, SQLAlchemy e Postgresql.
  
  Buscando atender os requisitos, este projeto apresenta um servidor inspirado na arquitetura REST para a consulta e inserção de registros.
  As validações de integridade de dados (limite de três carros por cidadão, por exemplo) foram concentradas no banco de dados.
  
### Arquivos Principais

* **./init.sql** -> Inicialização do banco. Definição dos relacionamentos, integridade de dados e validações.
* **./Dockerfile_db** : Dockerfile para o serviço do banco de dados Postgresql.
* **./norktown/app.py** : Configurações iniciais do SQLAlchemy e loader dos controllers, de acordo com a requisição HTTP e o método.
* **./norktown/citizen/ControllerCitizen.py** : Trata as requisições do domínio 'URL/citizen', 
    comunicando-se com o modelo './norktown/citizen/ModelCitizen.py' quando necessário comunicar-se com o banco.
* **./norktown/vehicle/ControllerVehicle.py** : Trata as requisições do domínio 'URL/vehicle', 
    comunicando-se com o modelo './norktown/citizen/ModelVehicle.py' quando necessário comunicar-se com o banco.
 
### Exemplos de Requisições

[GET] http://localhost:8080/citizen : Retorna todos os registros de cidadãos de Norktown.

[GET - parâmetro de URL 'cpf'] http://localhost:8080/citizen?cpf=05195702942 : Retorna o cidadão portador do CPF '05195702942'.

[GET - parâmetro de URL 'id'] http://localhost:8080/citizen?id=1 : Retorna o cidadão com o ID = '1', referente à tabela no banco de cidadãos.

[GET] http://localhost:8080/vehicle : Retorna todos os registros de veículos de Norktown.

[GET - parâmetro de URL 'cpf'] http://localhost:8080/vehicle?cpf=05195702942 : Retorna todos os registros de veículos associados ao cidadão com o cpf fornecido como parâmetro.

[GET - parâmetro de URL 'plate'] http://localhost:8080/vehicle?plate=PZ65PWO : Retorna o veículo com placa 'PZ65PWO'.

[GET - parâmetro de URL 'id'] http://localhost:8080/vehicle?id=1 : Retorna o veículo com o ID = '1', referente à tabela no banco de veículos.

[POST - parâmetros de formulário 'name', 'cpf', 'address'] http://localhost:8080/citizen : Insere registro de cidadão de acordo com os parâmetros de formulário preenchidos no corpo da requisição. Campo 'address' é opcional.

[POST - parâmetros de formulário 'cpf', 'plate', 'model', 'color'] http://localhost:8080/vehicle : Insere registro de veículo de acordo com os parâmetros de formulário preenchidos no corpo da requisição. Campo 'cpf' é referente ao proprietário do veículo, e deve estar associado a um registro de cidadão.




  
