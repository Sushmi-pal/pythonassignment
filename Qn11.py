type=input('Enter a sentence: ')
lower_name=type.lower()
typesplit=lower_name.split(' ')
a=len(typesplit)
b=dict()
for i in range(a):
    count=typesplit.count(typesplit[i])
    b[typesplit[i]] = count

print(b)