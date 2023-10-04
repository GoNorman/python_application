
class Resource:
    def __init__(self, type, name, speed):
        self.type = type #name and max speed
        self.name = name
        self.speed = speed

    def display_info(self):
        return (f"{self.type.display_info()} {self.name} {self.speed}")
        

