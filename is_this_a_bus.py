class vehicle:
    def __init__(self,name,maximum_speed,millage):
        self.name=name
        self.maximum_speed=maximum_speed
        self.millage=millage
        
class bus(vehicle):
    pass
school_bus=bus("school volvo",180,12000)
print("vehicle name:",school_bus.name,",max speed is",school_bus.maximum_speed,",millage is",school_bus.millage)
