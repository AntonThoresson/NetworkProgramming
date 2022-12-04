import queue
class Node:
    def __init__(self, prio, data):
        self.prio = prio
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.prio < other.prio

    def __str__(self):
        return "({} {})".format(self.prio, self.data)

class Huffman:
    def __init__(self, text):
        self.dict = {}
        self.txt = self.readFile(text)
        self.txt = bytearray(self.txt, "UTF-8")
        self.prob = self.makeProb(self.makeHisto(self.txt))
        self.pq = queue.PriorityQueue()
        self.fillQueue(self.prob, self.txt)

    def readFile(self,text):
        with open(text, "r") as file:
            txt = file.read()
        return txt

    def makeHisto(self, byteArr):
        histo = [0] * 256
        for byte in byteArr:
            histo[byte] += 1
        return histo

    def makeProb(self,histo):
        probDist = [0.0] * 256
        totalSumOfProbDist = 0
        for i in range(256):
            probDist[i] += histo[i]/len(self.txt)
            totalSumOfProbDist += probDist[i]
        print(totalSumOfProbDist)
        return probDist

    def fillQueue(self, prob, text):
        for i in range(256):
            self.pq.put(Node(prob[i], text[i]))

    def buildHuffamTree(self):
        while self.pq.qsize() != 1:
            child1 = self.pq.get()
            child2 = self.pq.get()

            parent = Node(child1.prio+child2.prio, None)
            parent.left = child1
            parent.right = child2

            self.pq.put(parent)


    def assignValues(self):
        root = self.pq.get()
        value = ""
        self.findCodeLength(root, value)

    def findCodeLength(self, node, value):
        if (node == None):
            return
        if (node.data != None):
            self.dict[value] = node.data

        self.findCodeLength(node.left, value + "0")
        self.findCodeLength(node.right, value + "1")

test = Huffman("text.txt")
# test.buildHuffamTree()
# test.assignValues()
i = 0
# for key, value in test.dict.items():
    # if (test.prob[i] != 0):
        # pl = len(key) * test.prob[i] 
        # print(key,":", value,"P(x)L(x): ", round(pl, 2))
    # i+=1












