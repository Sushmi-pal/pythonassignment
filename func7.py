def upperlower(st):
    countupper=0
    countlower=0
    s=len(st)
    for i in range(s):
        if st[i]==st[i].upper() and st[i]!=' ':
            countupper=countupper+1
        elif st[i]==st[i].lower() and st[i]!=' ':
            countlower=countlower+1
        else:
            continue

    print('Number of Uppercase Characters:',countupper)
    print('Number of Lowercase Characters:', countlower)
upperlower('The quick Brow Fox')