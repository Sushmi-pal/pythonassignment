li=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in li:
    print('The multiple of {}'.format(i))
    print(list(filter(lambda x:x%i==0,li)))