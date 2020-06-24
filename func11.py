x=lambda a:a+15
z=lambda x,y:x*y
a=int(input('Enter an integer to add with 15 '))
print('The result of addition with 15 is',end=' ')
print(x(a))
print('The result of multiplication of two numbers is',end=' ')
print(z(3,4))
