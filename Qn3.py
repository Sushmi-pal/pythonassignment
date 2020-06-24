name=input('Enter any string: ')
a=len(name)
b=name[0]
for i in range(1,a):
    if name[i] == name[0]:
        name = name.replace(name[i],'$')
        print(b+name[1:])

