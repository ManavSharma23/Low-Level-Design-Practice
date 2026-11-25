# Strategy Design Pattern
# It is a behavioral design pattern that defines a family of algorithms
# and puts each algorithm into a separate class.
# It allows us to switch between different algorithms at runtime.
# It promotes composition over inheritance and reduces conditional statements.
# Example: Different payment methods like UPI, Credit Card, and Cash.


from abc import ABC,abstractmethod

class DiscountStratergy(ABC):
    @abstractmethod

    def discount(self):
        pass


class Diwali(DiscountStratergy):
    def discount(self):
        print(f"19% Discount has been applied, [ Diwali ]")

class BlackFriday(DiscountStratergy):
    def discount(self):
        print(f"22% Discount has been applied, [ Black Friday ]")

class StudentDiscount(DiscountStratergy):
    def discount(self):
        print(f"18% Discount has been applied, [ Student Discount ]")

class First_Time(DiscountStratergy):
    def discount(self):
        print(f"16% Discount has been applied , [ First Time ]")


class Discount:
    def __init__(self,strategy):
        self.__stratergy=strategy
    
    def set_strategy(self,new_strategy):
        self.__stratergy=new_strategy

    def process(self):
        self.__stratergy.discount()

# Client side test

diwali=Diwali()
blackfriday=BlackFriday()
studentdiscount=StudentDiscount()
first_time=First_Time()

D1=Discount(first_time)

(D1.process())

D1.set_strategy(blackfriday)
D1.process()

