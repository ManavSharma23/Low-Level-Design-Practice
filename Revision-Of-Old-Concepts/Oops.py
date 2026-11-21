# class student:

#     #attributes 
#     class_No=4
#     school="MCS"
#     #constructor
    
#     def __init__(self,name: str,age: int,gender: str):
#         print("************Constructor Called**************")
#         self.name=name
#         self.age=age
#         self.gender=gender


#     #method with a parameter and arrow shows it return nothing

#     def display(self) -> None:
#         print("*********************")
#         print("This Is A Display Function")
#         print(f"The Name Is {self.name}")
#         print(f"The Age Is {self.age}")
#         print(f"The Gender Is {self.gender}")


#     def set_info(self) -> None:
#             self.name=input("Enter name: ")
#             self.age=int(input("Enter age: "))
#             self.gender=input("Enter gender: ")
        
 

# s1=student() # object is created
# print(s1)  # here the address is printed 
# print(s1.age)  # dot is used to acces a value 

# # setting values manually 
# s1.name="Arjun"
# s1.gender="male"
# print(s1.gender)

# s2=student()
# s2.name="Priya"
# s2.age=20
# s2.gender="female"

#  # using a function 
# s1.display()

# #setting values using a function but it wont be needed after constructor is made or 
# #if we have decided to use it to make some changes
# s3=student()
# s3.set_info()
# s3.display()

# #setting values using a constructor and we have to use this only 

# s4=student("Radhika",20,"Non-binary")
# s4.display()


#---------Inheritance--------

class Animal():

    def __init__(self,name,age):

        print("**********Constructor called")
        self.name=name
        self.age=age

    def sleep(self):
        print("Sleeping")
    
    def eating(self):
        print("Eating")


class Dog(Animal):

    def __init__(self,name,age,breed):
        super().__init__(name,age)
        print("child Constructor")                  # here we need a additonal thing called breed but we dont want to increase the code so we are calling the parent constructir to makw it 
        self.breed=breed
    def bark(self):
        print("Barking")

    def display(self):
        print("Name is : ",self.name)
        print("Age is : ",self.age)
        print("Breed is : ",self.breed)

    


d1=Dog('happy',5,'pomerian')
d1.sleep()
d1.eating()
d1.bark()
d1.display()


