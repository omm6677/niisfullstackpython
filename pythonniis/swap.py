#swapping two varibales using 3rd variables
'''
a=10
b=20
print("before swapping a=", a,"b=",b)
a=a+b
b=a-b
a=a-b
print("After swapping a=", a,"b=",b)
#swapping two varibales using 3rd variables

a=10
b=20
print("before swapping a=", a,"b=",b)
t=a
a=b
b=a
print("After swapping a=", a,"b=",b)

#swapping two varibales using 3rd variables
a=10
b=20
print("before swapping a=", a,"b=",b)
a=a^b
b=a^b
a=a^b
print("After swapping a=", a,"b=",b)

a=10
b=2.5
c="hi"
print(a,b,c)

a,b,c=10,2.5,"hi"
print(a,b,c)

a=10
b=20
a,b=b,a
print(a,b)

# swapping of 3 numbers using 4th variable (left to right)

a=10
b=20
c=30
print("before swapping a=",a,"b=",b,"c=",c)
f=c
c=b
b=a
a=f
print("after swapping a=",a,"b=",b,"c=",c)

print("e" in "hello")
print("x" in "hello")
print("x" not in "hello")
print(10 in [10,20,30,40])
print(40 in [10,20,30,40])
print(40 not in [10,20,30,40])
'''
a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)