from modul.resource_class import Resource
from modul.type_of_resource import Type_Of_Resource
from manager.manager import Manager
import json

sport_car = Type_Of_Resource("sport car", 250)

car_honda = Resource(sport_car, "Honda", 200)
car_porsche = Resource(sport_car, "Posrche", 200)

m1 = Manager

