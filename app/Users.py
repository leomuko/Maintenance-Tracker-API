from flask import Flask,request, abort, jsonify
import json
from models import USERS


User_table = USERS()



app = Flask(__name__)


@app.route('/auth/signup', methods= ['POST'])
def user_signup():
    Firstname = request.json.get('Firstname')
    Lastname = request.json.get('Lastname')
    Email = request.json.get('Email')
    password = request.json.get('password')
    User_table.create_new_user(Firstname, Lastname,Email,password)

    return jsonify({'Message': 'New User Created'})

@app.route('/auth/login', methods=['POST'])
def user_login():
    Email = request.json.get('Email')
    password = request.json.get('password')
    User_table.login_user(Email, password)
    return jsonify({'Message':'You have successfully logged in'})
    




    
    
    




if __name__ == '__main__':
    app.run(debug=True)