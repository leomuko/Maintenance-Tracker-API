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



@app.route('/users/requests/<int:requestId>', methods=['GET'])
def view_specific_request(requestId):
   requestId = request.json.get('requestId')
   Request_table.specific_request(requestId)



    
   

















if __name__ == '__main__':
    app.run(debug=True)