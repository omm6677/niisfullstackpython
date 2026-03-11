class Interest:
    def __init__(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t
    def show(self):
        print("Principal =", self.p)
        print("Rate =", self.r)
        print("Time =", self.t)
    def sical(self):
        return self.p*self.r*self.t/100
i1 = Interest(1000,5,2)
i2 = Interest(2000,4,3)
i1.show()
i2.show()
print("simple interest=",i1.sical())