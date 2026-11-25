# Template Method Design Pattern
# It is a behavioral design pattern where the parent class defines the steps of a task.
# Child classes implement specific steps according to their needs.
# The parent decides the order in which the steps are performed.
# It avoids writing the same code again and again.
# Example: Processing JSON, CSV and Binary files using the same steps.


from abc import ABC,abstractmethod

class template(ABC):

    def open(self):
        print(f"File is opening")

    @abstractmethod    
    def parse(self):
        pass

    def close(self):
        print(f"File is closing")
        print(f"****************************************")

    def process_file(self):
        self.open()
        self.parse()
        self.close()

class json(template):
    def parse(self):
        print("parsing the [JSON] file")       

class csv(template):
    def parse(self):
        print("parsing the [Csv] file")

class binary(template):
    def parse(self):
        print("parsing the [Binary] file")
        
json=json()
json.process_file()

csv=csv()
csv.process_file()

binary=binary()
binary.process_file()