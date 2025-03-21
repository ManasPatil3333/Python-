'''
class Person :
    name = "Robot 2.0"
    def info(self) :
        print(f"{self.name} is a Good Engineer")

a = Person()
a.name = "Manas"
a.info()
'''

class Student :
    def __init__(self, name, workExp) :
        self.name = name
        self.workExp = workExp
    
    def getName(self) :
        return self.name
    
    def getWorkExp(self) :
        return self.workExp
    
    def setName(self, value) :
        self.name = value

    def setWorkExp(self, value) :
        self.workExp = value

    def info(self) :
        print(f"I am {self.name} and I have {self.workExp} years work experience.")
        print(self.name + self.workExp )

a = Student(7,2) 
a.info()
