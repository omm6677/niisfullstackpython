print("enter a number")
no=int(input())
if no>0:
	print("+ve")
elif no<0:
	print("-ve")
else:
	print("zero")

"""wap to take a number from keyboard to check no is sd dd td od +ve number check"""

print("Enter number")
no=int(input())
if no>0:
	if n<10:
		print("single digit number")
	elif n<100:
		print("double digit number")
	elif n<1000:
		print("Three digit number")
	else:
		print("other digit number")
else:
	print("not a positive number")
