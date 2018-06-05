from flask import Flask,request, abort, jsonify
import json
from models import *

NewUser = Users()

app = Flask(__name__)


@app.route('/auth/signup', methods= ['POST'])
def user_signup():
    Firstname = request.json.get('Firstname')
    Lastname = request.json.get('Lastname')
    Email = request.json.get('Email')
    password = request.json.get('password')
    NewUser.create_new_user(Firstname, Lastname,Email,password)
    return jsonify({'Message': 'New User Created'})
    
    




if __name__ == '__main__':
    app.run(debug=True)