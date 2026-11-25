# Command Design Pattern
# It is a behavioral design pattern that turns a request into a separate object.
# It encapsulates a request as an object, allowing us to parameterize,
# queue, execute, and undo operations independently.
# It separates the object that makes a request from the object that performs it.
# Example: Remote control buttons, where each button represents a command.



from abc import ABC,abstractmethod

class order(ABC):
    @abstractmethod
    def execute(self):
        pass

class chef:
    def cook_burger(self):
        print("Burger Order Taken")
    
    def cook_pizza(self):
        print("Pizza Order Taken")

    def cook_pasta(self):
        print("Pasta Order Taken")

    def cook_kulcha(self):
        print("Kulcha Order Taken")

class burger(order):

    def __init__(self,chef):
        self.__chef=chef

    def execute(self):
        self.__chef.cook_burger()

class pizza(order):
    def __init__(self,chef):
        self.__chef=chef

    def execute(self):
        self.__chef.cook_pizza()

class pasta(order):
    def __init__(self,chef):
        self.__chef=chef

    def execute(self):
        self.__chef.cook_pasta()

class kulcha(order):
    def __init__(self,chef):
        self.__chef=chef

    def execute(self):
        self.__chef.cook_kulcha()

class Waiter:
    def place_order(self,thing):
        thing.execute()

chef=chef()

order1=burger(chef)
order2=pizza(chef)
order3=pasta(chef)
order4=kulcha(chef)

waiter=Waiter()
waiter.place_order(order1)
waiter.place_order(order2)
waiter.place_order(order3)
waiter.place_order(order4)
