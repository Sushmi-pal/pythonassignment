li=[]
num=int(input('Enter number of items in list'))
for i in range(num):
    listitem=int(input('Enter an integer: '))
    li.append(listitem)
result=1
print(li)
for i in li:
    result=result*i

print('The result is {}'.format(result))