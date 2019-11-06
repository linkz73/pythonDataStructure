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
    global front, rear, size
    res = None
    if size != 0:
        res = front.item
        front = front.next
        size -= 1
        if size == 0:
            rear = None
    else:
        print("underflow!! 출력불가")

    return res


def printQ():
    if size == 0:
        print("Queue is empty!")
        return

    print("Front <=\t", end="")
    p = front
    while p:

        if p.next is not None:
            print(p.item, "<=", end="")
        else:
            print(p.item, '<= rear')

        p = p.next

