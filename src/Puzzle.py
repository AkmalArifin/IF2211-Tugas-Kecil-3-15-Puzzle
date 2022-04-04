import time
from PriorityQueue import PriorityQueue


# Constant Value
GOAL_STATE = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

def readFile(matrixPuzzle, fileName):
    lines = []
    dir = '../test/' + fileName
    with open(dir, 'r') as f:
        lines = f.readlines()

    i = 0
    for line in lines:
        parse = line.split(' ', 4)
        arrayPuzzle = []
        arrayPuzzle.append(int(parse[0]))
        arrayPuzzle.append(int(parse[1]))
        arrayPuzzle.append(int(parse[2]))
        arrayPuzzle.append(int(parse[3]))
        matrixPuzzle.append(arrayPuzzle)

def listToString(li):
    text = ""
    for num in li:
        text += str(num)
        text += " "
    text += "\n"
    return text

def writeFile(path, fileName, totalNode, time):
    dir = '../test/' + fileName
    f = open(dir, "w")

    for matriks in path:
        for row in matriks:
            text = listToString(row)
            f.write(text)
        f.write("\n")

    for row in GOAL_STATE:
        text = listToString(row)
        f.write(text)
    f.write("\n")
    f.write(f"Waktu yang dibutuhkan : {time}\n")
    f.write(f"Jumlah node yang dibangktikan : {totalNode}\n")


def estimateCost(matrixPuzzle):
    jumlahKurang = 0
    for i in range(4):
        for j in range(4):
            if (matrixPuzzle[i][j] == 16):
                continue
            if(matrixPuzzle[i][j] != GOAL_STATE[i][j]):
                jumlahKurang += 1
    return jumlahKurang

def kurang(matrixPuzzle):
    jumlahKurang = 0
    for i in range(4):
        for j in range(4):
            num = matrixPuzzle[i][j]
            for k in range(i, 4):
                for l in range(4):
                    if (i == k and l < j):
                        continue
                    elif (num > matrixPuzzle[k][l]):
                        jumlahKurang += 1
    return jumlahKurang

def isSolveable(matrixPuzzle):
    sum = kurang(matrixPuzzle)
    print(sum)
    for i in range(4):
        for j in range(4):
            if matrixPuzzle[i][j] == 16:
                sum += (i+j)%2
    print(sum)
    return sum % 2 == 0


def bangkitkan(queue, totalNode):
    i0 = queue.getEmptyi()
    j0 = queue.getEmptyj()
    matrixRise = queue.getMatrix()
    path = []
    pathRise = queue.getPath()
    if (len(pathRise) > 0):
        for i in range(len(pathRise)):
            tempPath = [[0 for j in range(4)] for i in range(4)]
            for j in range(4):
                for k in range(4):
                    tempPath[j][k] = pathRise[i][j][k]
            path.append(tempPath)
    path.append(queue.getMatrix())
    queue.delete()

    try:
        matrixUp = [[0 for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                matrixUp[i][j] = matrixRise[i][j]
        temp = matrixUp[i0][j0]
        matrixUp[i0][j0] = matrixUp[i0-1][j0]
        matrixUp[i0-1][j0] = temp

        costUp = len(path) + estimateCost(matrixUp)

        iUp = i0-1
        jUp = j0
        if (not matrixUp in path):
            queue.insert(costUp, iUp, jUp, matrixUp, path)
            totalNode += 1
    except IndexError:
        # print("index error")
        pass
    
    try:
        matrixRight = [[0 for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                matrixRight[i][j] = matrixRise[i][j]
        temp = matrixRight[i0][j0]
        matrixRight[i0][j0] = matrixRight[i0][j0+1]
        matrixRight[i0][j0+1] = temp

        costRight = len(path) + estimateCost(matrixRight)

        iRight = i0
        jRight = j0+1

        if (not matrixRight in path):
            queue.insert(costRight, iRight, jRight, matrixRight, path)
            totalNode += 1
    except IndexError:
        # print("index error")
        pass
    
    try:
        matrixDown = [[0 for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                matrixDown[i][j] = matrixRise[i][j]
        temp = matrixDown[i0][j0]
        matrixDown[i0][j0] = matrixDown[i0+1][j0]
        matrixDown[i0+1][j0] = temp

        costDown = len(path) + estimateCost(matrixDown)

        iDown = i0+1
        jDown = j0

        if (not matrixDown in path):
            queue.insert(costDown, iDown, jDown, matrixDown, path)
            totalNode += 1
    except IndexError:
        # print("index error")
        pass

    try:
        matrixLeft = [[0 for j in range(4)] for i in range(4)]
        for i in range(4):
            for j in range(4):
                matrixLeft[i][j] = matrixRise[i][j]
        temp = matrixLeft[i0][j0]
        matrixLeft[i0][j0] = matrixLeft[i0][j0-1]
        matrixLeft[i0][j0-1] = temp

        costLeft = len(path) + estimateCost(matrixLeft)

        iLeft = i0
        jLeft = j0-1

        if (not matrixLeft in path):
            queue.insert(costLeft, iLeft, jLeft, matrixLeft, path)
            totalNode += 1
    except IndexError:
        # print("index error")
        pass
    
    return queue, totalNode
    

def checkGoal(matrixPuzzle):
    isSame = True
    for i in range(4):
        for j in range(4):
            if (matrixPuzzle[i][j] != GOAL_STATE[i][j]):
                isSame = False
    
    return isSame

def branchAndBound(matrixPuzzle):
    queue = PriorityQueue()
    cost = estimateCost(matrixPuzzle)
    totalNode = 1

    for i in range(4):
            for j in range(4):
                if matrixPuzzle[i][j] == 16:
                    i0 = i
                    j0 = j

    queue.insert(cost, i0, j0, matrixPuzzle, [])
    isFound = False
    while(not isFound and not queue.isEmpty()):
        queue,totalNode = bangkitkan(queue, totalNode)
        if (checkGoal(queue.getMatrix())):
            goalPath = queue.getPath()
            isFound = True
    if (isFound):
        return goalPath, totalNode
    else:
        return [], totalNode

def main():
    matrixPuzzle = []
    readFile(matrixPuzzle, "3.txt")
    
    if (isSolveable(matrixPuzzle)):
        tStart = time.time()
        goalPath, totalNode = branchAndBound(matrixPuzzle)
        tEnd = time.time()
        writeFile(goalPath, "solusi.txt", totalNode, tEnd-tStart)
    else:
        print("unsolveable")

main()