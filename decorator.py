class question :
    def __init__(self, num1, num2) :
        self.a = num1
        self.b = num2
    
    def greet(fx) :
        def mfx(*args,**kwargs) :
            print("All The Best!\n")
            fx(*args,**kwargs)
        return mfx
    
    def getb(self) :
        return self.b
    
    def geta(self) :
        return self.a
    
    def seta(self,value) :
        self.a = value
    
    def setb(self,value) :
        self.b = value
    
    @greet
    def add(self) :
        print(self.a+self.b) 

ques = question(10,20)
ques.add()