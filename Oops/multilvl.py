#multilevel inheritance
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("class person")
	def show_person(self):
		print("Name :",self.name)
		print("age :",self.age)
class Student(Person):
	def __init__(self,name,age,roll):
		super().__init__(name,age)
		self.roll = roll
	def show_student(self):
		print("Roll no:",self.roll)

class EngineeringStudent(Student):
	def __init__(self,name,age,roll,branch):
		super().__init__(name,age,roll)
		self.branch=branch
	def show_engg(self):
		print("branch:",self.branch)

e=EngineeringStudent("Rahul(not manisha's bf)",20,101,"computer Science")
e.show_person()
e.show_student()
e.show_engg()