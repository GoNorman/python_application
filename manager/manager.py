import json

list_resource = list()
list_resource_type = list()

class Manager:

    def __init__(self):
        self.id = id

    def create_resource(resource):
        list_resource.append(resource)
        return list_resource.index(resource)
    
    def change_resource(id, resource):
        list_resource[id] = resource
    
    def delete_resource(resource):
        list_resource.pop(list_resource.index(resource))

    def get_id(resource):
        return list_resource.index(resource)
    
    def create_new_type(res_of_type):
        list_resource_type.append(res_of_type)
        return list_resource_type.index(res_of_type)

    def show_dict():
        print(list_resource)

    def create_json(resource):
        json_x = {
            "type" : [{
                "name" : resource.type.name,
                "max_speed" : resource.type.max_speed
            }],
            "name" : resource.name,
            "speed" : resource.speed

        }

