
from abc import ABC,abstractmethod

class ATC(ABC):
    @abstractmethod
    def send_message_in_ATC(self):
        pass

    @abstractmethod    
    def register_plane(self):
        pass
    

class ControlTower(ATC):
    def __init__(self):
        self.__planes=[]

    def register_plane(self,plane_No):
        self.__planes.append(plane_No)

    def send_message_in_ATC(self,msg,airplane):
        for i in self.__planes:
            if i.get_id()!=airplane.get_id():
                i.receive_message(msg,airplane)

class Airplane:
    def __init__(self,plane_id,ControlTower):
        self.__id=plane_id
        self.__ct=ControlTower
        self.__ct.register_plane(self)

    def get_id(self):
        return self.__id
    
    def send_message(self,msg):
        self.__ct.send_message_in_ATC(msg,self)
    
    def receive_message(self,msg,incoming_id):
        print(f"Message from Plane ID: {incoming_id.get_id()}\nRecieved Successfully by: {self.__id}\nMsg Is: {msg}")
        print("***********************************")
        print()



CT1=ControlTower()
Boeing777=Airplane("Boeing777",CT1)
AirbusA320=Airplane("AirbusA320",CT1)
Rafeal=Airplane("Rafeal",CT1)

Boeing777.send_message("Hello , I AM LANDING ON PATH 7 . CLEAR THE LANDING SPOT BEFORE 20 MINUTES ")

