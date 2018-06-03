import unittest
import json
from app import api


class TestRequests(unittest.TestCase):
    def setup(self):
        self.testing = api.app.test_client()

    def test_get_all_requests(self):
        response = self.testing.get('/app/v1/users/requests')
        self.assertEqual(response.status_code, 201)

    def test_get_single_request(self):
        requestId = json.loads(self.testing.data)["requestId"]
        response = self.testing.get('/api/v1/users/requests/{}/'.format(requestId))
        self.assertEqual(response.status_code, 201)  
        

    def test_create_request(self):
        response = self.testing.get('/api/v1/users/requests')
        self.assertEqual(response.status_code, 201)


    def test_modify_request(self):
        requestId = json.loads(self.testing.data)["requestId"]
        response = self.testing.get('/api/v1/users/requests/{}/'.format(requestId))
        Request = json.loads(response.data)["Request"]
        newRequest = json.loads(response.data)
        newRequest["Request"] = Request    
        self.assertEqual(response.status_code, 201)

















if __name__=='__main__':
    unittest.main()