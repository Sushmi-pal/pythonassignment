def checkindict(d1,k):
    if k in d1.keys():
        print('Present and the value is ',d1[k])
    else:
        print('Not Present')

checkindict({1:10,2:20,'a':30},'a')#For present key
checkindict({1:10,2:20,'a':30},'b')#For absent key