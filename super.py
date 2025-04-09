class Employee() :
    def __init__(self, name, id) :
        self.name = name
        self.id = id
    
class Programmer(Employee) :
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def display(self) :
        print(f"Name : {self.name}\nId : {self.id}\nProgramming Language : {self.lang}.")

Employee1 = Programmer("Manas Kiran Patil", "682", "Python")
Employee1.display()
Employee2 = Programmer("Vignesh P", "678","Java")
Employee2.display()