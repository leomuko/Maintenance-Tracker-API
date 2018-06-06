from flask import Flask,request, abort, jsonify, make_response
import json
from models import USERS
import jwt 
from functools import wraps
from models import Requests


Request_table = Requests()


User_table = USERS()


app = Flask(__name__)
app.config['SECRET KEY'] = 'thisissecret'


def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'token_access' in request.headers:
            token = request.headers['token_access']
        if not token:
            return jsonify({'message':'Missing token'}) 
        try:
            data = jwt.decode(token, app.config['SECRET KEY'])
            current_user = data

        except:
            return jsonify({'message':'Invalid Token'}) 
        return f(current_user, *args, **kwargs)
    return decorated

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
    if not User_table.login_user(Email,password):
        return jsonify({'message':'wrong password and email'})
    else:
        token = jwt.encode({'Email':Email}, app.config['SECRET KEY'])   
        return jsonify({'token':token.decode('UTF-8')})

@app.route('/users/requests',methods=['POST'])
@token_required
def create_user_request(current_user):
    Email = request.json.get('Email')
    Userid = User_table.get_user_Id(Email)
    RequestType = request.json.get('RequestType')
    RequestDetails = request.json.get('Details')
    Request_table.create_new_user_request(Userid,RequestType,RequestDetails)
    return jsonify({'message':'Request created successfully'})



@app.route('/users/requests', methods=['GET'])
@token_required
def view_all_requests(current_user):
   Email = request.json.get('Email')
   Userid = User_table.get_user_Id(Email)
   return jsonify(Request_table.all_requests_for_specific_user(Userid))


@app.route('/users/requests/<int:Request_id>', methods=['GET'])
@token_required
def view_specific_request(current_user,Request_id):
    return jsonify(Request_table.specific_request(Request_id))

  


@app.route('/users/requests/<int:Request_id>', methods=['PUT'])
@token_required
def modify_user_request(current_User,Request_id):
    R_type = request.json.get('RequestType')
    R_details = request.json.get('Details')
    Request_table.modify_request(Request_id,R_type,R_details) 
    return jsonify({'message':'Request successfully modified'})        

    




    
    
    




if __name__ == '__main__':
    app.run(debug=True)