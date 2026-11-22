# Association
class person():
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name


class teacher(person) :
    def __init__(self,name,id):
        super().__init__(name)        #using get name function from parent class person
        self.__id=id

    def get_id(self):
        return self.__id

    def teach(self,student):        #teacher is calling student name here its association
        print(f"{self.get_name()} teaches {student.get_name()}")

class student(person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.__roll_no=roll_no

    def get_roll_no(self):
        return self.__roll_no


class department():

    def __init__(self,name):
        self.__deptname=name
        self.__students_data=[]

    def add_student(self,student):
        self.__students_data.append(student)
    
    def show_name(self):
        return self.__deptname

    def show_students(self):
        print(f"Students in {self.show_name()} are : ")
        for i in self.__students_data:
            print(i.get_name())



t1=teacher("john",123)
s1=student("kalam",23)

print(s1.get_roll_no())   
print(t1.get_name())

t1.teach(s1)

cs=department("Computer Science")
cs.add_student(s1)
cs.show_students()    

