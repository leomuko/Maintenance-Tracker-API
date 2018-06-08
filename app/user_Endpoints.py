from flask import Flask,request, abort, jsonify, make_response
import json
from models import USERS
import jwt 
from functools import wraps
from models import Requests
import re
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
Request_table = Requests()


User_table = USERS()

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
    hashed_password = generate_password_hash(password)
    if not Firstname:
        return jsonify({'Message':'Please Enter FisrtName'})
    elif not isinstance(Firstname, basestring) :
        return jsonify({'message':'Firstname must be string'})    
    elif not Lastname:
        return jsonify({'Message':'Please Enter LastName'})
    elif not isinstance(Lastname,basestring):
        return jsonify({'message':'Lastname must be string'})      
    elif not Email:
        return jsonify({'Message':'Please Enter Email'})
    elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]", Email):
        return jsonify({'Message':'Enter valid Email'})
    elif not password:
        return jsonify({'Message':'Please Enter Password'})
    elif len(password) < 4:
        return jsonify({'message':'Enter stronger password'})  
    else:
       User_table.create_new_user(Firstname, Lastname,Email,hashed_password)
       return jsonify({'Message': 'New User Created'}), 201

@app.route('/auth/login', methods=['POST'])
def user_login():
    Email = request.json.get('Email')
    password = request.json.get('password')
    hashed_password = User_table.retrieve_user_password(Email)
    if not check_password_hash(hashed_password,password):
        return jsonify({'message':'Enter correct password'})
    elif not User_table.login_user(Email,hashed_password):
        return jsonify({'message':'Please check your email or password'})
    else:
        token = jwt.encode({'Email':Email}, app.config['SECRET KEY'])   
        return jsonify({'token':token.decode('UTF-8')}),201
             

@app.route('/users/requests',methods=['POST'])
@token_required
def create_user_request(current_user):
    Email = request.json.get('Email')
    password = request.json.get('password')
    RequestType = request.json.get('RequestType')
    RequestDetails = request.json.get('Details')
    
    if not Email:
        return jsonify({'Message':'Please Review your Email'})
    elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]", Email):
        return jsonify({'Message':'Please Review your Email'})
    elif Email != current_user['Email']:
        return jsonify({'Message':'Enter valid Email'})
    else: 
        hashed_password = User_table.retrieve_user_password(Email)

    if not check_password_hash(hashed_password,password): 
        return jsonify({'message':'please enter valid password'})
    elif not RequestType:
        return jsonify({'message':'Please enter Request Type'})
    elif not isinstance(RequestType,basestring):
        return jsonify({'message':'RequestType must be string'})      
    elif not RequestDetails:
        return jsonify({'message':'Please Enter Request Details'})
    elif not isinstance(RequestDetails,basestring):
        return jsonify({'message':'RequestDetails must be string'})      
    else:
        Userid = User_table.retrieve_user_Id(Email)
        Request_table.create_new_user_request(Userid,RequestType,RequestDetails)
        return jsonify({'message':'Request created successfully'}),200


@app.route('/users/requests', methods=['GET'])
@token_required
def view_all_requests(current_user):
   Email = current_user['Email']
   Userid = User_table.retrieve_user_Id(Email)
   req= Request_table.all_requests_for_specific_user(Userid)
   if len(req) == 0:
       return jsonify({'message':'You have no requests'})    
   else:
       return jsonify(req)


@app.route('/users/requests/<int:Request_id>', methods=['GET'])
@token_required
def view_specific_request(current_user,Request_id):
    Email = current_user['Email']
    Userid = User_table.retrieve_user_Id(Email)
    spec_requests = Request_table.specific_request(Request_id,Userid)
    if len(spec_requests) == 0:
        return jsonify({'message':'You do not have a request by that id. Please review your requests and enter valid request Id'})
    else:    
        return jsonify(spec_requests)
   
@app.route('/users/requests/<int:Request_id>', methods=['PUT'])
@token_required
def modify_user_request(current_user,Request_id):
    R_type = request.json.get('RequestType')
    R_details = request.json.get('Details')
    inputEmail = request.json.get('Email')
    Email = current_user['Email']
    password = request.json.get('password')
    Userid = User_table.retrieve_user_Id(Email)
    request_check = Request_table.specific_request(Request_id, Userid)
    if len(request_check) == 0:
        return jsonify({'message':'You do not have a request by that id. Please review your requests and enter valid request Id'})
    elif not inputEmail:
        return jsonify({'Message':'Please Enter your Email'})
    elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]", inputEmail):
        return jsonify({'Message':'Please Review your Email'})
    elif inputEmail != current_user['Email']:
        return jsonify({'Message':'Enter valid Email'})
    else:
        hashed_password = User_table.retrieve_user_password(Email)
    
    if not check_password_hash(hashed_password,password): 
        return jsonify({'message':'please enter valid password'})
    elif not R_type:
        return jsonify({'message':'Enter request type'})
    elif not isinstance(R_type,basestring):
        return jsonify({'message':'Request Type must be string'})      
    elif not R_details:
        return jsonify({'message':'Enter request details'})
    elif not isinstance(R_details,basestring):
        return jsonify({'message':'Request Details must be string'})     
    elif Request_table.check_if_request_exists(Userid, Request_id) is False:
        return jsonify({'message':'You do not have access to the request'})   
    else:   
       Request_table.modify_request(Request_id,R_type,R_details) 
       return jsonify({'message':'Request successfully modified'})        

    




    
    
    




if __name__ == '__main__':
    app.run(debug=True)