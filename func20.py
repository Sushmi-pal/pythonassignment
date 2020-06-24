num1 = [1, 2, 3, 5, 7, 8, 9, 10]
num2 = [8,9,10,11,12]
print("Original arrays:")
print(num1)
print(num2)
result = list(filter(lambda x: x in num1,num2))
print ("\nIntersection of arrays: ",result)
