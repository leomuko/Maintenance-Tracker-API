from flask import Flask, request, jsonify
from models import Administrator
from functools import wraps
import jwt
import json

Admin = Administrator()


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
            admin = data

        except:
            return jsonify({'message':'Invalid Token'}) 
        return f(admin, *args, **kwargs)
    return decorated





@app.route('/auth/admin/login', methods=['POST'])
def admin_login():
    Email = request.json.get('Email')
    password = request.json.get('password')

    if not Email:
        return jsonify({'message':'Please Enter Email'})

    elif not password:
        return jsonify({'message':'Wrong password'})

    elif Email != 'admin@admin':
        return jsonify({'message':'Please enter correct Email'})
    elif password != 'password':
        return jsonify({'message':'Please enter correct password'})
    else:
        token = jwt.encode({'Email':Email}, app.config['SECRET KEY'])   
        return jsonify({'token':token.decode('UTF-8')})


@app.route('/admin/requests', methods=['GET'])
@token_required
def all_requests(admin):
    all_user_requests = Admin.get_all_requests()
    if len(all_user_requests) == 0:
        return jsonify({'message': 'There are no User requests'})    
    else:    
        return jsonify(all_user_requests)

@app.route('/admin/requests/<requestId>/approve', methods=['PUT'])
@token_required
def approve_request(admin,requestId):
    all_user_requests = Admin.get_all_requests()
    if len(all_user_requests) == 0:
        return jsonify({'message': 'There are no User requests'}) 
    elif Admin.check_for_request(requestId) is False:
        return jsonify({'message':'Request does not exist'})
    else:   
        Admin.approve_request(requestId)
        return jsonify({'message':'Successfully approved'})

@app.route('/admin/requests/<requestId>/disapprove', methods=['PUT'])
@token_required
def disapprove_request(admin,requestId):
    all_user_requests = Admin.get_all_requests()
    if len(all_user_requests) == 0:
        return jsonify({'message': 'There are no User requests'}) 
    elif Admin.check_for_request(requestId) is False:
        return jsonify({'message':'Request does not exist'})
    else:   
        Admin.disapprove_request(requestId)
        return jsonify({'message':'Successfully approved'})

@app.route('/admin/requests/<requestId>/resolve', methods=['PUT'])
@token_required
def resolve_request(admin,requestId):
    all_user_requests = Admin.get_all_requests()
    if len(all_user_requests) == 0:
        return jsonify({'message': 'There are no User requests'}) 
    elif Admin.check_for_request(requestId) is False:
        return jsonify({'message':'Request does not exist'})
    else:   
        Admin.disapprove_request(requestId)
        return jsonify({'message':'Successfully approved'})







if __name__ == '__main__':
    app.run(debug=True)