listitem=[]
num=int(input('Enter number of items in list: '))
for i in range(num):
    textnum=int(input('Enter an integer: '))
    listitem.append(textnum)
print('The maximum number is',max(listitem))