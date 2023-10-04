import json

list_resource = list()
list_resource_type = list()

class Manager:

    def __init__(self):
        self.id = id

    def create_resource(resource):
        list_resource.append(resource)
        return list_resource.index(resource)
    
    def create_resource_bd(request, conn):
        data = request.get_json()
        name = data.get('name')
        current_speed = data.get('current_speed')
        type_id = data.get('type_id')

        cursor = conn.cursor()
        cursor.execute(
        "INSERT INTO resource (name, current_speed, type_id) VALUES (%s, %s, %s)",
        (name, current_speed, type_id)
        )
        conn.commit()

        return {"message": "Resource created successfully"}
    
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
        print(json.dumps(json_x))
        return json.dumps(json_x)
    
    def get_all_resources(request, conn):
        cursor = conn.cursor()
        cursor.execute(
        "SELECT r.id, r.name, r.current_speed, rt.name as type_name, rt.max_speed FROM resource r INNER JOIN resource_type rt ON r.type_id = rt.id"
        )
        resources = cursor.fetchall()
        result = []
        for row in resources:
            resource_data = {
                "id": row[0],
                "name": row[1],
                "current_speed": row[2],
                "type_name": row[3],
                "max_speed": row[4]
            }
            result.append(resource_data)
        return {"resources": result}

