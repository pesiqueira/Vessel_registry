import unittest
from obj.vessel_class import Vessel

class VesselClassTest(unittest.TestCase):
    vessel_dict = {'code':'AB201', 'items':[]}
    vessel = Vessel(vessel_dict)
    item = {'code':'1234B1C7','location':'Brasil', 'name': 'Motor'}
    
    def test_get_code(self):
        self.assertEqual(self.vessel.get_code(), 'AB201')
    
    def test_isValidCode(self):
        self.assertTrue(self.vessel.isValidCode('AB201'))
        self.assertTrue(self.vessel.isValidCode('AB211'))
        self.assertTrue(self.vessel.isValidCode('QQ101'))
        self.assertFalse(self.vessel.isValidCode('A1201'))
        self.assertFalse(self.vessel.isValidCode('1B201'))
        self.assertFalse(self.vessel.isValidCode('AB2013'))
        self.assertFalse(self.vessel.isValidCode('aBB201'))
    
    def test_get_info(self):
        self.assertEqual(self.vessel.get_info(),self.vessel_dict)

    def test_set_get_item(self):
        self.vessel.set_item(self.item)

        get_item = self.vessel.get_item(self.item['code'])
        self.assertEqual(get_item,self.item)

        self.vessel.deactivate_item('1234B1C7')
        
        item = self.vessel.get_item('1234B1C7')
        self.assertEqual(item['active'],False)
    
    # def test_deactivate_item(self):
    
    def test_isValidItemCode(self):
        self.assertTrue(Vessel.isValidItemCode('1234B1V1'))

if __name__ == '__main__':
    unittest.main()