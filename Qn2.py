name=input('Enter any string:')
a=len(name)
if a>4:
    print(name[0:2]+name[-2:])
elif a==2:
    print(name+name)
else:
    print('Empty string')


