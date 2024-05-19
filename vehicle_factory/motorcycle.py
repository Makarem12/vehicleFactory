from vehicle_factory.factory import factory

class motorcycle (factory):

    motorcycle_count=0
    def __init__(self,number_of_wheels,model_name,fuel_type):
        super().__init__(model_name,fuel_type)
        self.number_of_wheels = 2
        motorcycle.motorcycle_count +=1
        self.set_fuel_type(fuel_type)

    #method to print how many motorcycles have been created
    @classmethod
    def get_count(cls): 
        print(motorcycle.motorcycle_count) 
       

    def read_attribute(self, attribute_name):
        if hasattr(self, f"_{attribute_name}"):
            return getattr(self, f"_{attribute_name}")
        else:
            raise AttributeError(f"'motorcycle' object has no attribute '{attribute_name}'")

    
    def __str__(self):
        return super().__str__()