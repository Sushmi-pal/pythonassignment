num=int(input('Enter the number of items in a list: '))
li=[]
new=[]
for i in range(num):
    text=input('Enter a string')
    li.append(text)
for x in li:
    if x not in new:
        new.append(x)
print(new)