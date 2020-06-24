name=input('Enter a string: ')
name1=name.replace(name[0:1],name[-1:])
name2=name.replace(name[-1:],name[0:1])
print(name1[0:1]+name[1:-1]+name2[-1:])