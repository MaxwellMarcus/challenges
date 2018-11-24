import random

def sort(num,smallest=True):
    olen = len(num)

    ans = []

    added = False

    if smallest:
        i = 0
        while len(num) > 0:
            added = False
            if len(num) == olen:
                ans.append(num[0])
                num.remove(num[0])
                added = True
            elif num[0] < ans[0]:
                ans.insert(0,num[0])
                num.remove(num[0])
                added = True
            else:
                i = 0
                while i < len(ans):
                    if num[0] < ans[i]:
                        ans.insert(i,num[0])
                        num.remove(num[0])
                        added = True
                        break
                    i += 1

            if not added:
                ans.append(num[0])
                num.remove(num[0])
    else:
        i = 0
        while len(num) > 0:
            added = False
            if len(num) == olen:
                ans.append(num[0])
                num.remove(num[0])
                added = True
            elif num[0] > ans[0]:
                ans.insert(0,num[0])
                num.remove(num[0])
                added = True
            else:
                i = 0
                while i < len(ans):
                    if num[0] > ans[i]:
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
    matrix = matrix
    i = 0
    newMatrix = []
    while i < len(matrix):
        newMatrix.append(list(matrix[i]))
        i += 1
    matrix = newMatrix
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
            if sub[q] == '1' and not started:
                started = True
                spot = [i,q]
                longestLine += 1
            elif started:
                if sub[q] == '1':
                    lines += [[longestLine,spot]]
                    longestLine += 1
                if sub[q] == '0':
                    lines += [[longestLine,spot]]
                    longestLine = 0
                    started = False
            q += 1
        if started:
            lines += [[longestLine,spot]]
        i += 1

    q = 0
    while q < len(lines):
        line = lines[q]
        height = 0
        z = 0
        while z < line[0]:
            b = 0
            while b < len(lines):
                if lines[b][1][0] == line[1][0] + z and lines[b][0] == line[0]:
                    height += 1
                    b += 1
                    if height == line[0]:
                        squares.append([height*line[0],line[1]])
                b += 1
            z += 1
        q += 1

    i = 0
    while i < len(squares):
        if squares[i][0] > ans:
            ans = squares[i][0]
        i += 1
    return ans

def KaprekarsConstant(num):
    done = False
    newNum = num
    loops = 0
    while loops < 5:
        if newNum == 6174:
            done = True
        else:
            ascending = sort(list(str(newNum)))
            descending = sort(list(str(newNum)),False)
            newNum = int(descending) - int(ascending)
            if len(str(newNum)) < 4:
                newNum = str(newNum) + '0'
                newNum = int(newNum)
        loops += 1

    return loops

def closestEnemy(matrix):
    enemyLocations = []
    i = 0
    while i < len(matrix):
        k = 0
        sub = list(matrix[i])
        while k < len(sub):
            if sub[k] == '2':
                enemyLocations += [(k,i)]
            if sub[k] == '1':
                location = (k,i)
            k += 1
        i += 1

    i = 0
    ans = []
    while i < len(enemyLocations):
        colJump = False
        rowJump = False
        x,y = None,None
        if location[0] + abs(len(sub) - enemyLocations[i][0]) < abs(enemyLocations[i][0] - location[0]):
            rowJump = True
        if location[1] + abs(len(matrix) - enemyLocations[i][1]) < abs(enemyLocations[i][1] - location[1]):
            colJump = True
        if rowJump:
            x = location[0] + abs(len(sub) - enemyLocations[i][0])
        if colJump:
            y = location[1] + abs(len(matrix) - enemyLocations[i][1])
        if x == None:
            x = abs(location[0]-enemyLocations[i][0])
        if y == None:
            y = abs(location[1]-enemyLocations[i][1])
        ans += [x + y]
        i += 1
    return min(ans)

def eightQueens(l):
    i = 0
    includedSquares = []
    while i < len(l):
        queen = []
        up,down,loops = False,False,1
        while not up or not down:
            if not up:
                if not l[i][0] + loops == 0 and not True:
                    queen.append(l[i][0])
            loops += 1

def biggestSquareMatrixEfficient(matrix):
    matrix = list([[int(x) for x in s] for s in matrix])

    i = 0
    while i < len(matrix):
        k,sub = 0,matrix[i]
        while k < len(sub):
            if sub[k] == '1':
                squared = False
                height = 1
                while not squared:
                    pass
        i += 1
print(biggestSquareMatrixEfficient(["0111", "1101", "0111"]))
