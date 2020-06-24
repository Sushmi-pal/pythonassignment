def checkprime(num):
    count=0
    for i in range(1,num+1,1):
        n=num%i
        if n==0:
            count=count+1
    if count==2:
        print('prime')
    else:
        print('composite')

checkprime(11)