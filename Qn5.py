name=input('Enter a string: ')
if len(name)>=3 and name[-3:]!='ing':
    print(name+'ing')

elif len(name)>=3 and name[-3:]=='ing':
    print(name+'ly')

else:
    print(name)