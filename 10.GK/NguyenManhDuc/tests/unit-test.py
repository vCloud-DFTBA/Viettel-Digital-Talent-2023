import unittest
import requests
import os


base_host = os.environ.get('API_HOST', 'http://localhost')
base_port = os.environ.get('API_POST', '5500')


class TestCandidatesAPI(unittest.TestCase):
    
    port_id = ''

    def __init__(self, *args, **kwargs) -> None:
        super(TestCandidatesAPI, self).__init__(*args, **kwargs)
        self.mockdata = {
            "STT": 0,
            "fullname": "TESTing this shit",
            "year of birth": 2002,
            "gender": "Nam",
            "university": "academy of cryptography techniques",
            "Username": "testxx",
            "field": "cyber security"
        }
        response=requests.post(f'{base_host}:{base_port}/candidates',json=self.mockdata)
        data = response.json()
        self._id = data['_id']
        print("DONE")

    
    def test_post_candidate(self):
        test_mock_data = {
            "STT": 0,
            "fullname": "data for post",
            "year of birth": 2003,
            "gender": "Nữ",
            "university": "academy of cryptography techniques",
            "Username": "testxx",
            "field": "cyber security"
        }
        response=requests.post(f'{base_host}:{base_port}/candidates',json=test_mock_data)
        data = response.json()
        self.port_id = data['_id']
        print("DONE")
        
        
   
    def test_get_all_candidates(self):
        response1=requests.get(f'{base_host}:{base_port}/candidates')
        response2=requests.get(f'{base_host}:{base_port}/')
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response2.status_code,200)
        self.assertGreater(len(response1.json()), 0)
        self.assertGreater(len(response2.json()), 0)   
        print("DONE")
          
        
    def test_get_one_candidate(self):
        # print(self._id)
        response = response = requests.get(f'{base_host}:{base_port}/candidates/{self._id}')
        self.assertEqual(response.status_code,200)
        self.assertGreater(len(response.json()),0)
        print("DONE")
        
    def test_put_change_candidate(self):
        mock_data_change ={
            "STT": 0,
            "fullname": "test this shit change",
            "year of birth": 2010,
            "gender": "Nữ",
            "university": "harvard",
            "Username": "testYY",
            "field": "stream"
        }
        response = requests.put(f"{base_host}:{base_port}/candidates/update/{self._id}",json=mock_data_change)
        responseget=requests.get(f'{base_host}:{base_port}/candidates/{self._id}')
        data=responseget.json()
        self.assertEqual(response.status_code,200)
        self.assertEqual(data[0]["fullname"],mock_data_change["fullname"])
        self.assertEqual(data[0]["year of birth"],mock_data_change["year of birth"])
        self.assertEqual(data[0]["gender"],mock_data_change["gender"])
        self.assertEqual(data[0]["university"],mock_data_change["university"])
        self.assertEqual(data[0]["Username"],mock_data_change["Username"])
        self.assertEqual(data[0]["field"],mock_data_change["field"])
        print("DONE")
        
      
        
    def test_delete_candicate(self):
        response = requests.delete(f"{base_host}:{base_port}/candidates/{self._id}")
        self.assertEqual(response.status_code,200)
        print("DONE")
        
    
                
    def tearDown(self) -> None:
        response=requests.delete(f'{base_host}:{base_port}/candidates/{self._id}')
        response=requests.delete(f'{base_host}:{base_port}/candidates/{self.port_id}')
        return super().tearDown()

if __name__ == '__main__':
	# suite = unittest.TestLoader().loadTestsFromTestCase(TestCandidatesAPI)
	# unittest.TextTestRunner().run(suite)
    unittest.main()