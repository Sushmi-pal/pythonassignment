name=input('Enter a string: ')
namerep=name
lengthofname=len(name)
a=name.find('not')
b=name.find('poor')

if a<b :
    name=name.replace(name[a:b+4],'good')
    print(name)

else:
    print(namerep)