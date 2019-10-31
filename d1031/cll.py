# Circular Linked List

class CLList:

    class Node:
        def __init__(self, name, link):
            self.name = name
            self.link = link

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertFront(self, name):
        if self.isEmpty():
            self.head = self.Node(name, None)
            self.tail = self.Node(name, None)