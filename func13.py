x=[(2,1),(3,5),(4,2),(6,3),(5,4)]
print('Before sorting:',x)
x.sort(key=lambda x:x[1])
print('After sorting:',x)