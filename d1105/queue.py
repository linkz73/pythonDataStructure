class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


front = rear = None
size = 0


def enQue(item):
    global front, rear, size
    new = Node(item, None)
    if size == 0:
        front = rear = new
    else:
        rear.next = new
        rear = new

    size += 1

def deQue():
    pass

def printq():
    pass