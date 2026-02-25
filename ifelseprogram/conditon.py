#wap to check if number is positie or negative , provide 0 no output
print("enter a number")
no=int(input())
if no!=0:
	if no>0:
		print("+ve")
	else:
		print("-ve")

#wap to check if number is positie or negative , provide 0 no output
print("enter a number")
no=int(input())
if no!=0:
	if no>0:
		print("+ve")
	else:
		print("-ve")
else:
	print("zero")


#wap take 3 no from keybord display biggest number
print("enter 3 numbers")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first no is bigger",no1)
	else:
		print("third number is bigger",no3)
else:
	if no2>=no3:
		print("second number is bigger",no2)
	else:
		print("third number is bigger",no3)
