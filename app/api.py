from flask import Flask,request, abort, jsonify
import json 

app = Flask(__name__)


Requests = [{ 'requestId': 1,
              'requestType': 'Laundry',
              'details': 'My laundry machine is faulty'

}]

@app.route('/api/v1/users/requests', methods=['POST'])
def create_request():
    if not request.json or not "requestType" in request.json:
        abort(400)
    Request = { 'requestId': Requests[-1]['requestId'] + 1 ,
              'requestType': request.json.get('requestType'),
              'details': request.json.get('details', ''),
             }    
    Requests.append(Request)
    return  jsonify('Request', Request), 201

@app.route('/api/v1/users/requests', methods=['GET'])
def get_requests():
    return jsonify({'Request': Requests}), 200

@app.route('/api/v1/users/requests/<int:requestId>', methods=['GET'])
def get_request_by_id(requestId):
    Request = [Request for Request in Requests if Request['requestId'] == requestId ]
    if len(Request) == 0:
        return abort(400)
    return jsonify({'Request': Request}), 200  

@app.route('/api/v1/users/requests/<int:requestId>', methods=['PUT'])
def modify_request(requestId):
    Modify = [Request for Request in Requests if Request['requestId'] == requestId] 
    if len(Modify) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'details' in request.json and type(request.json['details']) is not unicode:
        abort(400)  
   
    Modify[0]['requestType'] = request.json.get('requestType', Modify[0]['requestType'])
    Modify[0]['details'] = request.json.get('details', Modify[0]['requestType'])
    return jsonify({'Request': Modify[0]})      
   



    






if __name__ == '__main__':
    app.run(debug=True)