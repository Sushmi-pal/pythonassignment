listitem=[]
count=0
num=int(input('Enter number of items in list: '))
for i in range(num):
    textstr=input('Enter a string: ')
    listitem.append(textstr)
print(listitem)
for i in listitem:
    if i[0]==i[-1]:
        count=count+1
print('The result is',count)
