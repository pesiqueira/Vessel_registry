from dao.vessel import Dao
import unittest
import json
dao = Dao()
unittest.TestLoader.sortTestMethodsUsing = None
class DaoVesselTest(unittest.TestCase):
    vessel_dict = {'code':'AB201', 'items':[]}
    item = {'code':'1234B1C7','location':'Brasil', 'name': 'Motor'}
    
    def test_create_get_vessel(self):
        """Create a vessel using dao function"""
        res = dao.create_vessel(self.vessel_dict)
        self.assertEqual(res,'created')
        
        with self.subTest("Get"):
            """Getting all vessels from dao"""
            res = dao.get_vessel()
            self.assertEqual(res,json.dumps([self.vessel_dict]))

        with self.subTest("Search"):
            """Getting a specific vessel from dao"""
            res = dao.search_vessel_code('AB201')
            self.assertEqual(res, self.vessel_dict)
    
    def test_delete_vessel(self):
        """Deletting a specific vessel from dao"""
        res = dao.delete_vessel(self.vessel_dict['code'])
        self.assertEqual(res,'deleted')

if __name__ == '__main__':
    unittest.main()