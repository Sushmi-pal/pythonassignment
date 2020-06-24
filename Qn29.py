def adddict(d1,d2,d3):
    print(d1)
    print(d2)
    print(d3)
    d1.update(d2)
    d1.update(d3)
    print(d1)

adddict({1:10,2:20},{3:30,4:40},{5:50,6:60})