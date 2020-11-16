import json
ITEM_NOT_FOUND ='Item not found'
class Vessel():
    def __init__(self, vessel_json):
        vessel_dict = vessel_json
        if self.isValidCode(vessel_dict['code']):
            self.code = vessel_dict['code']
            if 'items' in vessel_dict:
                self.items = vessel_dict['items'] 
            else:
                self.items =[]
        else:
            raise NameError('Invalid Code')

    def get_code(self):
        return self.code

    def get_info(self):
        all_atributes = {
            "code": self.code,
            "items": self.items
        }
        return all_atributes
    
    def set_item(self, item):
        if(item['name'] and item['code'] and item['location']):
            active_item = item
            if(self.isValidItemCode(item['code'])):
                if(self.get_item(item['code'])==ITEM_NOT_FOUND):
                    active_item['active'] = True
                    self.items.append(active_item)
            else:
                return 'invalid item code'

    def get_item(self,item_code):
        for item in self.items:
            if item['code'] == item_code:
                return item
        return ITEM_NOT_FOUND
    
    def get_all_items(self):
        return self.items
    
    def delete_item(self,item_code):
        item = self.get_item(item_code)
        self.items.remove(item)
        return 'deleted'
    
    def deactivate_item(self,item_code):
        item = self.get_item(item_code)
        if(item == 'Item not found'):
            return 'Item Not Found'
        else:
            item['active'] = False
            return 'deactivated'

    @staticmethod
    def isValidCode(code):
        if code and len(code)==5 and code[0:2].isalpha() and code[2:5].isnumeric():
            return True
        else:
            return False

    @staticmethod
    def isValidItemCode(item_code):
        if (item_code and len(item_code)==8 and item_code[0:4].isnumeric() and item_code[5].isnumeric() and item_code[7].isnumeric() and item_code[4].isalpha() and item_code[6].isalpha()):
            return True
        else:
            return False