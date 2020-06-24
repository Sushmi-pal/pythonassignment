name=input('Enter any string ')
c=name.lower()
print(c)
a=len(name)
i=0
b=dict()


for i in range(a):
    count=c.count(c[i])
    b[c[i]] = count

print(b)
