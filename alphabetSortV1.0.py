def alphabetSort(string):
    #string is a string that will be sorted in alphabetic order

    alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

    num = string
    num = list(num)

    olen = len(num)

    ans = []

    added = False

    i = 0
    while len(num) > 0:
        added = False
        if len(num) == olen:
            ans.append(num[0])
            num.remove(num[0])
            added = True
        elif alphabet[num[0]] < alphabet[ans[0]]:
            ans.insert(0,num[0])
            num.remove(num[0])
            added = True
        else:
            i = 0
            while i < len(ans):
                if alphabet[num[0]] < alphabet[ans[i]]:
                    ans.insert(i,num[0])
                    num.remove(num[0])
                    added = True
                    break
                i += 1

        if not added:
            ans.append(num[0])
            num.remove(num[0])
    i = 0
    final = ''
    while i < len(ans):
        final += ans[i]
        i += 1
    ans = final
    return ans

print(alphabetSort(input('string: ')))
