class Employee :
    def __init__(self, name, age, department) :
        self.name = name
        self.age = age
        self.department = department

    @classmethod
    def fromStr (cls, string) :
        name, age, department = string.split("-")
        return cls(name, int(age), department)
    
    def display(self) :
        print(f"I  am {self.name} from '{self.department}' department. I am {self.age} years old.")

E1 = Employee.fromStr("Manas Kiran Patil-18-Computer and Science Engneering")
E1.display() 

