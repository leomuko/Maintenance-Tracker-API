from flask import Flask,request, abort, jsonify
import json
from models import Requests


Request_table = Requests()




app = Flask(__name__)

@app.route('/users/requests',methods=['POST'])
def create_user_request():
    Userid = request.json.get('UserId')
    RequestType = request.json.get('RequestType')
    RequestDetails = request.json.get('Details')
    Request_table.create_new_user_request(Userid,RequestType,RequestDetails)
    return jsonify({'message':'Request created successfully'})



@app.route('/users/requests', methods=['GET'])
def view_all_requests():
   return jsonify(Request_table.view_all_requests())


@app.route('/users/requests/<int:Request_id>', methods=['GET'])
def view_specific_request(Request_id):
    return jsonify(Request_table.specific_request(Request_id))


@app.route('/users/requests/<int:Request_id>', methods=['PUT'])
def modify_user_request(Request_id):
    R_type = request.json.get('RequestType')
    R_details = request.json.get('Details')
    Request_table.modify_request(Request_id,R_type,R_details) 
    return jsonify({'message':'Request successfully modified'})   



    
   

















if __name__ == '__main__':
    app.run(debug=True)