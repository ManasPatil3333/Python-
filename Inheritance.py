class Parent :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def getName(self) :
        return self.name
    
    def getAge(self) :
        return self.age
    
    def setName(self, value) :
        self.name = value

    def setAge(self, value) :
        self.age = value

class Child (Parent) :
    def __init__(self, name, age, gender):
        self.gender = gender
        Parent.__init__(self,name,age)

    def display(self) :
        print(f"I am {self.name} and I am {self.age} years old.\nGender : {self.gender}")

a = Child("Manas",18,"Male")
a.display()