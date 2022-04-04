class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, dataCost, i, j, dataMatrix, dataPath):
        self.queue.append([dataCost, i, j, dataMatrix, dataPath])

    def getCost(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min][0]
            return item
        except IndexError:
            print()
            exit()
    
    def getMatrix(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min][3]
            return item
        except IndexError:
            print()
            exit()
    
    def getPath(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min][4]
            return item
        except IndexError:
            print()
            exit()

    def getEmptyi(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min][1]
            return item
        except IndexError:
            print()
            exit()

    def getEmptyj(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min][2]
            return item
        except IndexError:
            print()
            exit()

    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            del self.queue[min]
        except IndexError:
            print()
            exit()

    def print(self):
        print(self.getCost())
        print(self.getMatrix())
        print(self.getPath())