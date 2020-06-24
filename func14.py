listofdict=[{'name':'Ram','age':30},{'name':'Shyam','age':29},{'name':'Hari','age':32},
            {'name':'Sunil','age':27},{'name':'Roni','age':22}]
listofdict.sort(key=lambda listofdict:listofdict['age'])
print(listofdict)