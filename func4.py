def revstring(s):

    # i=s.index(s[-1])
    j=len(s)-1
    for i in range(j,-1,-1):
        st=''.join(s[i])
        print(st,end='')
revstring('1234abcd')
