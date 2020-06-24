li=[]
def evenlist(l):
    for i in l:
        if i%2==0:
            li.append(i)
    print(li)

evenlist([1,2,3,4,5,6,7,8,9])