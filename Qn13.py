text=input('Enter a number of words separated by comma: ')
li=[]
sforstring=''
textinlist=text.split(',')
for x in textinlist:
    if x not in li:
        li.append(x)
li.sort()
print(li)
sforstring=','.join(li)
print(sforstring)