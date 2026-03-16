class vehicle:
    def __init__(self,max_speed,millage):
        self.max_speed=max_speed
        self.millage=millage
mercades=vehicle(80,60000)
print("The mercades's max speed is",mercades.max_speed,".The mercades's millage is",mercades.millage)