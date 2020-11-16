import json
class Vessel():
    def __init__(self, vessel_json):
        vessel_dict = vessel_json
        if self.isValidCode(vessel_dict['code']):
            self.code = vessel_dict['code']
            self.items = []
        else:
            raise NameError('Invalid Code')

    def get_code(self):
        return self.code
        
    @staticmethod
    def isValidCode(code):
        if code and len(code)==5 and code[0:2].isalpha() and code[2:5].isnumeric():
            return True
        else:
            return False

    def get_info(self):
        all_atributes = {
            "code": self.code,
            "items": self.items
        }
        return all_atributes
    
    def set_item(self, item):
        if(item['name'] and item['code'] and item['location']):
            if(self.isValidItemCode(item['code'])):
                if(not self.get_item(item['code'])):
                    self.items.append(item)
            else:
                return 'invalid item code'

    def get_item(self,item_code):
        for item in self.items:
            if item['code'] == item_code:
                return item
        return False

    @staticmethod
    def isValidItemCode(item_code):
        if (item_code and len(item_code)==8 and item_code[0:4].isnumeric() and item_code[5].isnumeric() and item_code[7].isnumeric() and item_code[4].isalpha() and item_code[6].isalpha()):
            return True
        else:
            return False