lis=[]
def addlist(li,str):
    for i in li:
        list='{0}{1}'.format(str,i)
        lis.append(list)
    print(lis)

addlist([1,2,3,4],'emp')