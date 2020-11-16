import json
import unittest
from app import app

class RegistryTestCase(unittest.TestCase):
    vessel_dict = {'code':'AB202', 'items':[]}
    item_dict = {'code':'1234B2C1','name':'Motor','location':'Brasil'}
    url = '/vessel'
    def setUp(self):
        self.app = app.test_client()
        self.app.post(self.url,json=self.vessel_dict)
    
    def test_registry_vessel_item(self):
        """Creating vessel items"""
        url = self.url + '/' + self.vessel_dict['code'] + '/items'

        self.app.post(url,json={'code':'1234B2C3','name':'Motor','location':'Brasil'})

        self.app.post(url,json={'code':'1234B2C2','name':'Motor','location':'Brasil'})
        
        res = self.app.post(url,json={'code':'1234B2C1','name':'Motor','location':'Brasil'})
        self.assertEqual(res.status_code,200)

        data = res.data

        self.assertEqual(data,'created'.encode('utf-8'))

        """ Getting all items of a Vessel"""
        res = self.app.get(self.url + '/' + self.vessel_dict['code'] + '/items')
        res_dict = json.loads(res.data)
        self.assertTrue(type(res_dict)==list)
        with self.subTest("Verify the code"):
            if len(res_dict):
                for vessel in res_dict:
                    self.assertTrue(vessel['code'])

        """ Getting a specific item of a Vessel"""
        res = self.app.get(self.url+'/'+self.vessel_dict['code']+'/items/'+self.item_dict['code'])
        res_data = json.loads(res.data)
        self.item_dict['active'] = True
        self.assertEqual(res_data,self.item_dict)

        """ Deactivate a specific item of a Vessel"""
        res = self.app.post(self.url+'/'+self.vessel_dict['code']+'/items/deactivate', json=[self.item_dict])
        data = res.data

        self.assertEqual(data,'deactivated'.encode('utf-8'))

        """ Deactivate multiples items of a Vessel"""
        res = self.app.post(self.url+'/'+self.vessel_dict['code']+'/items/deactivate', json=[{'code':'1234B2C2'},{'code':'1234B2C3'}])
        data = res.data
        self.assertEqual(data,'deactivated'.encode('utf-8'))

if __name__ == '__main__':
    unittest.main()