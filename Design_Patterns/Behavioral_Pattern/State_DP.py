# Strategy Design Pattern is a behavioral design pattern.
# It defines multiple algorithms and encapsulates them into separate classes.
# All strategies follow a common interface.
# Context uses the selected strategy and allows switching strategies at runtime.
# Reduces if-else conditions and promotes loose coupling.



from abc import ABC,abstractmethod

class TransportMethods(ABC):
    @abstractmethod 
    def ETA(self):
        pass

    @abstractmethod
    def direction(self):
        pass

class bike(TransportMethods):
    def __init__(self,eta,direction):
        self.__eta=eta
        self.__direction=direction

    def ETA(self):
        return self.__eta
    
    def direction(self):
        return self.__direction


class train(TransportMethods):
    def __init__(self,eta,direction):
        self.__eta=eta
        self.__direction =direction

    def ETA(self):
        return self.__eta
    
    def direction(self):
        return self.__direction

class car(TransportMethods):
    def __init__(self,eta,direction):
        self.__eta=eta
        self.__direction=direction

    def ETA(self):
        return self.__eta
    
    def direction(self):
        return self.__direction

class walking(TransportMethods):
    def __init__(self,eta,direction):
        self.__eta=eta
        self.__direction=direction

    def ETA(self):
        return self.__eta
    
    def direction(self):
        return self.__direction

class DirectionService:
    def __init__(self,mode):
        self.__mode=mode
    
    def get_eta(self):
        return self.__mode.ETA()

    def get_direction(self):
        return self.__mode.direction()


#client side

bike=bike("25 minutes","North")
train=train("1h 2m","South")
car=car("40 minutes","East")

direction_service=DirectionService(bike)
print(f"For Bike- \nETA: {direction_service.get_eta()}")
print(f"{direction_service.get_direction()}")

direction_service=DirectionService(car)
print(f"For Car- \nETA: {direction_service.get_eta()}")
print(f"{direction_service.get_direction()}")   

direction_service=DirectionService(train)
print(f"For Train- \nETA: {direction_service.get_eta()}")
print(f"{direction_service.get_direction()}")