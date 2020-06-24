def newlist(li):
    l=[]
    for i in li:
        if i not in l:
            l.append(i)
    print(l)

newlist([1,2,2,3,4,4,5])