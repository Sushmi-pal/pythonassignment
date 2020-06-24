d=dict()
d2=dict()
num=int(input('Enter the number of terms of dict1: '))
for i in range(num):
    key0fdict=input('Enter key of dict1[{}]'.format(i))
    value0fdict=input('Enter value of dict1[{}]'.format(i))
    d[key0fdict] =value0fdict


num2=int(input('Enter the number of terms of dict2: '))
for i in range(num2):
    key0fdict=input('Enter key of dict2[{}]'.format(i))
    value0fdict=input('Enter value of dict2[{}]'.format(i))
    d2[key0fdict]=value0fdict
d.update(d2)
print(d)
