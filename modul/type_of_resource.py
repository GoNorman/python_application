class Type_Of_Resource:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def getName(self):
        return self.name
    
    def get_max_speed(self):
        return self.speed

    def display_info(self):
        return (f"{self.name} {self.max_speed}")