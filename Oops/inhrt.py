class p:
	def __init__(self):
		print("pc")
class c(p):
	def __init__(self):

		super().__init__()
		print("cc")
ob=c()