# Observer Design Pattern:
# A behavioral design pattern that establishes a one-to-many relationship between objects.
# When the Subject changes its state, all registered Observers are automatically notified.
# Promotes loose coupling, as the Subject doesn't need to know the internal details of Observers.
# Example: YouTube notifications, Weather updates, Stock price alerts.


from abc import ABC, abstractmethod

class WeatherStation:
    def __init__(self):
        self.__observers=[]
        self.__temperature=0

    def notify(self):
        for i in self.__observers:
            i.update(self.__temperature)

    def update_temperature(self,temp):
        self.__temperature=temp
        self.notify()

    def add_observer(self,name):
        self.__observers.append(name)
    
    def remove_observer(self,name):
        self.__observers.remove(name)
    

class Observer(ABC):

    @abstractmethod
    def update(self,temp):
        pass


class Tv(Observer):
    def update(self,temp):
        print(f"Temp is updated on TV to {temp}")

class mobile(Observer):
    def update(self,temp):
        print(f"Temp is updated on mobile to {temp}")

class desktop(Observer):
    def update(self,temp):
        print(f"Temp is updated on desktop to {temp}")




Weather_Station=WeatherStation()
TV1=Tv()
MOBILE1=mobile()
DESKTOP=desktop()

Weather_Station.add_observer(TV1)
Weather_Station.add_observer(MOBILE1)
Weather_Station.add_observer(DESKTOP)

Weather_Station.update_temperature(23)
