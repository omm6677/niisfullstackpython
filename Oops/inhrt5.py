#multilevel inheritance
class Person:
	def f1(self):
		print("class person")
class Student(Person):
	def f2(self):
		print("class Student")
class EngineeringStudent(Student):
	def f3(self):
		print("class EngineeringStudent")
ob=EngineeringStudent()
ob.f1()
ob.f2()
ob.f3()