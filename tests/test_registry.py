import json
import unittest
from app import app

class RegistryTestCase(unittest.TestCase):
    vessel_dict = {'code':'AB202', 'items':[]}
    url = '/vessel'
    def setUp(self):
        self.app = app.test_client()
        self.app.post(self.url,json=self.vessel_dict)

    def test_registry_vessel(self):
        res = self.app.post(self.url,json={'code':'AB201'})
        self.assertEqual(res.status_code,200)
        data = res.data
        self.assertEqual(data,'created'.encode('utf-8'))

    def test_get_all_vessel(self):
        res = self.app.get(self.url)
        res_dict = json.loads(res.data)
        self.assertTrue(type(res_dict)==list)
        with self.subTest("Verify the code"):
            if len(res_dict):
                for vessel in res_dict:
                    self.assertTrue(vessel['code'])

    def test_get_vessel(self):
        res = self.app.get(self.url+'/'+self.vessel_dict['code'])
        res_data = json.loads(res.data)
        self.assertEqual(res_data,self.vessel_dict)

    def test_delete_vessel(self):
        res = self.app.delete(self.url+'/'+self.vessel_dict['code'])
        data = res.data
        self.assertEqual(data,'deleted'.encode('utf-8'))

if __name__ == '__main__':
    unittest.main()