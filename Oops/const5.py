#initializing the instance varibale using method
class Demo:
	def __init__(self,x,y): #method
		self.x=x#public instance variable
		self.__y=y #private instance variable 
	def show(self):
		print(ob.x)
		print(ob.__y)
ob=Demo(10,20)
#print(ob.x,ob.__y)
ob.show()