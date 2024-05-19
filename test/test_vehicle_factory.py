import pytest
from vehicle_factory.factory import factory
from vehicle_factory.motorcycle import motorcycle
from vehicle_factory.car import car

class DummyFactory(factory):
    def __init__(self, model_name, fuel_type):
        super().__init__(model_name, fuel_type)

    def __str__(self):
        return f"_model_name: {self._model_name}, _fuel_type: {self._fuel_type}"

    def read_attribute(self, attribute_name):
        if hasattr(self, f"_{attribute_name}"):
            return getattr(self, f"_{attribute_name}")
        else:
            raise AttributeError(f"'DummyFactory' object has no attribute '{attribute_name}'")

@pytest.fixture
def dummy_factory():
    return DummyFactory('TestModel', 'electric')

def test_factory_model_name(dummy_factory):
    assert dummy_factory.get_model_name() == 'TestModel'

def test_factory_fuel_type(dummy_factory):
    assert dummy_factory.get_fuel_type() == 'electric'

def test_factory_invalid_fuel_type():
    with pytest.raises(ValueError):
        DummyFactory('TestModel', 'invalid')

def test_factory_str(dummy_factory):
    assert str(dummy_factory) == '_model_name: TestModel, _fuel_type: electric'

# Car test
@pytest.fixture
def new_car():
    return car(4, 'ModelX', 'petrol', 'Red')

def test_car_invalid_doors():
    with pytest.raises(ValueError):
        car(3, 'ModelX', 'petrol', 'Red')

def test_car_count():
    car.car_count = 0
    car(4, 'ModelX', 'petrol', 'Red')
    car(2, 'ModelY', 'diesel', 'Blue')
    assert car.car_count == 2
    car.get_count()

# Motorcycle test
@pytest.fixture
def new_motorcycle():
    return motorcycle(2, 'ModelM', 'diesel')

def test_motorcycle_initialization(new_motorcycle):
    assert new_motorcycle.read_attribute('model_name') == 'ModelM'
    assert new_motorcycle.read_attribute('fuel_type') == 'diesel'

def test_motorcycle_count():
    motorcycle.motorcycle_count = 0
    motorcycle(2, 'ModelM', 'diesel')
    motorcycle(2, 'ModelN', 'electric')
    assert motorcycle.motorcycle_count == 2
    motorcycle.get_count()
