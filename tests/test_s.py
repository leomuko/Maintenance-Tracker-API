import unittest
import json
from app.user_Endpoints import app
from flask import Flask



class TestRequests(unittest.TestCase):
 
    def test_user_signup(self):
        self.client = app.test_client
        response = self.client().post('/auth/signup',  content_type="application/json", data = json.dumps(dict(FirstName = 'katwere', LastName = 'Leo', Email ='kat@gmail',password ='password'))) 
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client = app.test_client
        login_data = {'Email':'kat@gmail', 'password':'password'}
        response = self.client().post('/auth/login', content_type = "application/json", data = json.dumps(login_data))
        self.assertEqual(response.status_code, 201)  

        

    def test_create_request(self):
        self.client = app.test_client
        user_request ={ 
                        'RequestType': 'Pc shutdown',
                         'Details': 'My pc cant turn back on'
                       }    
        response = self.client().post('/users/requests',  content_type="application/json",data = json.dumps(user_request))
        self.assertEqual(response.status_code, 200)

   
















if __name__=='__main__':
    unittest.main()