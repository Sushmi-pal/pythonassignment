li=[]
num=int(input('Enter number of items in list'))
for i in range(num):
    listitem=int(input('Enter an integer: '))
    li.append(listitem)

print(li)
print('The sum of all the items is list is {}'.format(sum(li)))