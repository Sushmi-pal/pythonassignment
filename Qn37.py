def sumdict(d):
    multiplied=1
    for i in d.values():
        multiplied =i*multiplied
    print('The result of multiplication of all the values of dictionary is',multiplied)

sumdict({1:10,2:20,3:3})