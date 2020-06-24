def fact(num):
    factmul=1
    for i in range(num,0,-1):
        factmul=i*factmul
    print('The factorial of {} is {}'.format(num,factmul))

fact(4)

