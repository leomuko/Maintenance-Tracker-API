from flask import Flask,request, abort, jsonify


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
    Request = [Request for Request in Requests if Request['requestId'] == requestId ]
    if len(Request) == 0:
        return abort(400)
    if not request.json:
        return abort(400)
    Requests.remove(Request)    
    New_Request = { 'requestId': requestId,
                 'requestType': request.json.get('requestType'),
                 'details': request.json.get('details')
    }
    Requests.append(New_Request)    
    return jsonify({'Modified Request', New_Request}), 201



    






if __name__ == '__main__':
    app.run(debug=True)