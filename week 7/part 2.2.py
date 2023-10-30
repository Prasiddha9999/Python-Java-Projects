class Vehicle :
   max_speed = 0 
   mileage = 0 
   def __init__(self,max_speed,mileage):
     self.max_speed=max_speed
     self.mileage=mileage
    def Max_speedo(self):
     print(self.max_speed,'is the max speed')
    def mileag(self):
     print(self.mileage , 'is the mileage')   

 Car=Vehicle(21,45)
 Car.Max_speedo()
 Car.mileag()
