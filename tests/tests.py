import unittest
import json
from app.api import app
from flask import Flask


class TestRequests(unittest.TestCase):
    def setup(self):
        pass
 


    def test_get_all_requests(self):
        self.client = app.test_client
        response = self.client().get('api/v1/users/requests',  content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_single_request(self):
        self.client = app.test_client
        
        response = self.client().get('/api/v1/users/requests/1', content_type = "application/json")
        self.assertEqual(response.status_code, 200)  
        

    def test_create_request(self):
        self.client = app.test_client
        user_request ={ 
                        'requestType': 'Pc shutdown',
                         'details': 'My pc cant turn back on'
                       }    
        response = self.client().post('api/v1/users/requests',  content_type="application/json",data = json.dumps(user_request))
        self.assertEqual(response.status_code, 201)


    def test_modify_request(self):
        self.client = app.test_client
        user_request ={ 
                        'requestType': 'Pc shutdown',
                         'details': 'My pc cant turn back on'
                       }    
        response = self.client().put('/api/v1/users/requests/1', content_type = "application/json", data=json.dumps(user_request))
        self.assertEqual(response.status_code, 200)

















if __name__=='__main__':
    unittest.main()