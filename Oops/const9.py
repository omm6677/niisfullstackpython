class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
def show(s):
	print("my name =",s.name)
	print("my roll=",s.roll)
	print("my mark=",s.mark)
s=Student("muna",1,90.50)
show(s)