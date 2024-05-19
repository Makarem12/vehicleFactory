from abc import ABC, abstractmethod

class factory(ABC):
    def __init__(self, model_name, fuel_type):
        self._model_name = model_name
        self._fuel_type = None
        self.set_fuel_type(fuel_type)
        
    def set_model_name(self, new_model_name):
        self._model_name = new_model_name

    def get_model_name(self):
        return self._model_name
    
    def set_fuel_type(self, new_fuel_type):
        valid_fuel_types = ['electric', 'petrol', 'diesel']
        if new_fuel_type.lower() in valid_fuel_types:
            self._fuel_type = new_fuel_type.lower()
        else:
            raise ValueError(f"Invalid fuel type: {new_fuel_type}. Valid options are: {', '.join(valid_fuel_types)}")

    def get_fuel_type(self):
        return self._fuel_type

    @abstractmethod
    def read_attribute(self, attribute_name):
        pass
    
    def __str__(self):
        attributes = [f"{attr}: {getattr(self, attr)}" for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        return ", ".join(attributes)

