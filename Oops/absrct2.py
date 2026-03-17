from abc import *
class Shape(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,n,l,b):
        super().__init__(n)
        self.l=l
        self.b=b
    def area(self):
        print("Rectangle parameters:", self.l, self.b)
        return self.l*self.b
class Square(Shape):
    def __init__(self,n,s):
        super().__init__(n)
        self.s=s
    def area(self):
        print("Square parameter:", self.s)
        return self.s*self.s
class Triangle(Shape):
    def __init__(self,n,base,height):
        super().__init__(n)
        self.base=base
        self.height=height
    def area(self):
        print("Triangle parameters:", self.base, self.height)
        return 0.5*self.base*self.height
r1=Rectangle("Rectangle",5,7)
print("Area =",r1.area())
s1=Square("Square",6)
print("Area =",s1.area())
t1=Triangle("Triangle",4,8)
print("Area =",t1.area())