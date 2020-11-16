vessel_registry = []
from obj.vessel_class import Vessel
import json
INVALID_PARAM = 'Invalid parameter'
VESSEL_NF = 'Vessel Not Found'
class Dao():
    def create_vessel(self,vessel):
        vessel = Vessel(vessel)
        if(not self.search_vessel_code(vessel.get_code())):
            vessel_registry.append(vessel.get_info())
            return 'created'
        return 'Vessel code already registered'
        
    def get_vessel(self,code = ""):
        if(not code):
            return json.dumps(vessel_registry)
        else:
            vessel = self.search_vessel_code(code)
            if(vessel):
                return json.dumps(vessel)
            raise NameError("Code not found")
            
    def delete_vessel(self, code):
        if code:
            vessel = self.search_vessel_code(code)
            if(vessel):
                vessel_registry.remove(vessel)
                return 'deleted'
        raise NameError("Code not found")

    def search_vessel_code(self, code):
        for vessel in vessel_registry:
            if(vessel['code']==code):
                return vessel
        return False
    
    def get_vessel_item(self, code, item_code=""):
        if(code):
            found_vessel = self.search_vessel_code(code)
            if found_vessel:
                vessel = Vessel(found_vessel)
                if(item_code):
                    return vessel.get_item(item_code)
                else:
                    return vessel.get_all_items()
            else:
                return VESSEL_NF

    def insert_vessel_item(self, code, item):
        if(code and item):
            found_vessel = self.search_vessel_code(code)
            if found_vessel:
                vessel = Vessel(found_vessel)
                vessel_registry.remove(vessel.get_info())
                vessel.set_item(item)
                vessel_registry.append(vessel.get_info())
                return 'created'
            else:
                return VESSEL_NF
        else:
            return INVALID_PARAM
    
    def deactivate_vessel_item(self,code, item_code):
        if(code and item_code):
            found_vessel = self.search_vessel_code(code)
            if found_vessel:
                vessel = Vessel(found_vessel)
                return vessel.deactivate_item(item_code)
            else:
                return VESSEL_NF
        else:
            return INVALID_PARAM

    def delete_vessel_item(self, code, item_code):
        if(code and item_code):
            found_vessel = self.search_vessel_code(code)
            if found_vessel:
                vessel = Vessel(found_vessel)
                return vessel.delete_item(item_code)
            else:
                return VESSEL_NF
        else:
            return INVALID_PARAM