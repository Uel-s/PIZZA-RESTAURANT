class Vehicle:
    def printConsumer(self):
        print("none")

class MotorVehicle(Vehicle):
    def printConsumer(self):
        print("medium")

class Car(MotorVehicle):
    pass

car = Car()
car.printConsumer()

