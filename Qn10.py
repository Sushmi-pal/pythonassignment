name=input('Enter a string: ')
lenofstr=len(name)
s=''
for i in range(lenofstr):
    if (i %2!=0):
        continue
    else:
        s=s+name[i]
print(s)

