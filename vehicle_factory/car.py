from vehicle_factory.factory import factory

class car (factory):

    car_count=0
    def __init__(self,number_of_doors,model_name,fuel_type,car_color):
        super().__init__(model_name,fuel_type)
        self.set_number_of_doors(number_of_doors)
        self.car_color = car_color
        car.car_count +=1

    def set_car_color(self, new_car_color):
        self.car_color = new_car_color

    #method to print how many cars have been created
    @classmethod
    def get_count(cls): 
        print(car.car_count)

    def set_number_of_doors(self, number_of_doors):
        """ensuring it is either 2 or 4."""
        if number_of_doors not in [2, 4]:
            raise ValueError("Number of doors must be either 2 or 4")
        self.number_of_doors = number_of_doors            

    def read_attribute(self, attribute_name):
        if hasattr(self, f"_{attribute_name}"):
            return getattr(self, f"_{attribute_name}")
        else:
            raise AttributeError(f"'car' object has no attribute '{attribute_name}'")
 
    
    def __str__(self):
        return super().__str__()