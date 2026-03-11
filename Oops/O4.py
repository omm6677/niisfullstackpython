class Interest:
    def __init__(self,p,r,t):
        self.r = r
        self.t = t
    def show(self):
        print("Principal =", self.p)
        print("Rate =", self.r)
        print("Time =", self.t)
    def sical(self):
        return self.p*self.r*self.t/100
print("enter principle Rate and time")
pr=float(input())
r=float(input())
t=float(input())
i1=simp(pr,r,t)
i1.show()
print("simple interest=",i1.sical())