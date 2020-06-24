import copy
listitem=[]
num=int(input('Enter number of items in list: '))
for i in range(num):
    textstr=input('Enter a string: ')
    listitem.append(textstr)
print(listitem)
listcopy=copy.deepcopy(listitem)
print('Copied items of list',listcopy)