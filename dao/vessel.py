vessel_registry = []
from obj.vessel_class import Vessel
import json
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