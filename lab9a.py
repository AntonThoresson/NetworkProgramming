import queue   

class Node:
    def __init__(self, prio, data):
        self.prio = prio
        self.data = data

    def __lt__(self, other):
        return self.prio < other.prio

    def __str__(self):
        return "({} {})".format(self.prio, self.data)

def printAndPop(pq):
    while pq.qsize() > 0:
        print(pq.get())



def test1():
    print("Running test 1")
    pq = queue.PriorityQueue()
    pq.put(Node(4.0, 10))
    pq.put(Node(2.0, 8))
    pq.put(Node(5.0, 2))
    pq.put(Node(1.5, 8))
    pq.put(Node(4.0, 8))
    pq.put(Node(1.0, 8))
    pq.put(Node(3.0, (1,2)))
    pq.put(Node(2.0, (1,2)))
    printAndPop(pq)

#Tuple comparison breaks for (priority, symbol) pairs if the priorities are equal and the symbols do not have a default comparison order and thats whats happens
# when we compare (2,8) and (2,(1,2)).For equal priorities, Python then tries to compare a symbol from a leaf node (so the second element in a (priority, symbol)
# node tuple) with the (node, node) tuple from an inner node

test1()

