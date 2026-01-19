class square:

    def __init__(self,side):
        self.side = side

    def area(self):
        print("The area is", self.side**2)

osquare = square(5)
osquare.area()

class rectangle:

    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        print("The area is", self.height * self.width)

R = rectangle(2,10)
R.area()










