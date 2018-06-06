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
    Email = 'admin@admin'
    password = 'password'
    if not Email:
        return jsonify({'message':'Wrong email'})
    if not password:
        return jsonify({'message':'Wrong password'})    
    else:
        token = jwt.encode({'Email':Email}, app.config['SECRET KEY'])   
        return jsonify({'token':token.decode('UTF-8')})


@app.route('/admin/requests', methods=['GET'])
@token_required
def all_requests(admin):
    return jsonify(Admin.get_all_requests())

@app.route('/admin/requests/<requestId>/approve', methods=['PUT'])
@token_required
def approve_request(admin,requestId):
    Admin.approve_request(requestId)
    return jsonify({'message':'Successfully approved'})

@app.route('/admin/requests/<requestId>/disapprove', methods=['PUT'])
@token_required
def disapprove_request(admin,requestId):
    Admin.disapprove_request(requestId)
    return jsonify({'message':'Successfully disapproved'})

@app.route('/admin/requests/<requestId>/resolve', methods=['PUT'])
@token_required
def resolve_request(admin,requestId):
    Admin.resolve_request(requestId)
    return jsonify({'message':'Successfully resolved'})    







if __name__ == '__main__':
    app.run(debug=True)