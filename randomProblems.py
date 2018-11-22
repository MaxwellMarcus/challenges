import random

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

def biggestSquareMatrix(matrix):
    lines = []
    squares = []
    ans = 1
    i = 0
    while i < len(matrix):
        sub = matrix[i]
        longestLine = 0
        started = False
        q = 0
        while q < len(sub):
            if sub[q] == 1 and not started:
                started = True
                spot = [i,q]
                longestLine += 1
            elif started:
                if sub[q] == 1:
                    longestLine += 1
                if sub[q] == 0:
                    lines += [[longestLine,spot]]
                    longestLine = 0
                    started = False
            q += 1
        if started:
            lines += [[longestLine,spot]]
        i += 1
    i = 0
    while i < len(lines):
        q = 0
        line = lines[i]
        while q < len(lines):
            if lines[q][1][0] == line[1][0] + 1 and lines[q][0] == line[0]:
                height = 0
                z = 0
                while z < line[0] + 1:
                    b = 0
                    while b < len(lines):
                        if lines[q][1][0] == line[1][0] + z and lines[q][0] == line[0]:
                            height += 1
                            if height == line[0]:
                                squares.append([height**2,line[1]])
                        b += 1
                    z += 1


            q += 1
        i += 1

    i = 0
    while i < len(squares):
        if not squares[i][0] >= 4:
            squares.remove(squares[i])
        i += 1

    return squares

matrix = []
i = 0
while i < 100:
    k = 0
    subList = []
    while k < 10:
        subList.append(random.randint(0,1))
        k += 1
    matrix.append(subList)
    i += 1

i = 0
while i < 100:
    print(matrix[i])
    i += 1

print(biggestSquareMatrix(matrix))
