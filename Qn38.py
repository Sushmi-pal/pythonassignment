def remdict(d,k):
    if k in d.keys():
        del(d[k])
    print(d)

remdict({1:10,2:20,3:30},3)
remdict({1:10,2:20,3:30},5)