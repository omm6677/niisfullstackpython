print("enter basic salary")
s=int(input())
da,hr=0,0
da=a*0.3 if sal>=5000 else sal*0.2
hr=a*0.2 if sal>=5000 else sal*0.1
totalsal=a+da+hr	
print("salary of da =",da)
print("salary of hr =",hr)
print("total salary =",totalsal)