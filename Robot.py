class T:

    def __init__(self,name,age):
        self.name = name  
        self.age = age 
    
    def intro(self):
        print("Hi, I'm", self.name, "and", self.age, "Years old")



Tom = T("Tom", "Twelve")

Tom.intro()

class J:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("Hi I am", self.name, "and", self.age, "years old")

Jerry = J("Jerry", "10")

Jerry.intro()



