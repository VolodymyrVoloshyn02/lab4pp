from flask import Flask
from flask_restful import Resource, Api

from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controler import *

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'qwejhfloimslvuywdkkvuhssss'
jwt = JWTManager(app)
engine = create_engine('postgresql://postgres:1234@localhost/db11', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

    api.add_resource(AddUser, '/user')
    api.add_resource(Login, '/login')
    api.add_resource(GetUser, '/user/<int:id>')
    api.add_resource(GetMyself, '/user')
    api.add_resource(UpdateUser, '/user')

    api.add_resource(AddBank, '/bank')
    api.add_resource(GetBank, '/bank/<int:id>')

    api.add_resource(AddCredit, '/user/credit')
    api.add_resource(UpdateCredit, '/user/credit/<int:credit_id>')
    api.add_resource(GetCredit, '/user/credit/<int:credit_id>')

    api.add_resource(AddTransaction, '/user/credit/<int:credit_id>/transaction')
    api.add_resource(GetTransaction, '/user/credit/<int:credit_id>/transaction/<int:transaction_id>')

    app.run(debug=True)

"""{
   "username":"Vovik",
   "first_name":"Vova",
   "last_name":"Putin",
   "phone":"09348124",
   "email":"putin@gmail.com",
   "password":"123"
}"""


''' 
add bank
{
  "all_money": 500000,
  "per_cent" : 30
}
add user
{
    "login": "mylogin",
    "password": "my password",
    "name": "myname",
    "passport": "myUKRpasport",
    "address": "Lviv",
    "email": "user@gmail.com",
    "phone_number": "88005553535"
    "status": ""
}
add credit
{
    "start_date": "21.01.2020",
    "end_date": "21.01.2021",
    "start_sum": 1000,
    "current_sum": 100,
    "bank_id": 1,
    "user_id": 1
}
add transaction
{
    "date": "17.12.2020",
    "summ": 200
}

'''