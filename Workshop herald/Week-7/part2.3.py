class Vehicle:
    max_speed=0
    mileage=0

    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def speed(self):
        print(self.max_speed)
    def mile(self):
        print(self.mileage)
class Bus(Vehicle):
    pass
s=Bus(23,45)
s.speed()
s.mile()

        
