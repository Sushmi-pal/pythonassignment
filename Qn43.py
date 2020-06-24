def revfromtuple(t,i):
    if i in t:
        a=t.index(i)
    print(t[0:a]+t[a+1:])

revfromtuple((1,2,3,4,6,7),2)