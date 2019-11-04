

class DLList:
    class Node:
        def __init__(self, name, age, pre, next):
            self.name = name
            self.age = age
            self.pre = pre
            self.next = next

    def __init__(self):
        # self.head = self.Node(None, None, None, None)
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def searchNode(self, pos):
        p = self.head
        if pos is None:
            return None

        while p is not None:
            if p.name == pos:
                return p
            p = p.next

    def insert(self, name, age, pos=None):  #p 다음에 삽입
        p = self.searchNode(pos)
        # 최초 삽입
        if self.head is None:
            # new = self.Node(name, age, self.head, self.head)
            self.head = self.Node(name, age, None, None)

        # 첫 노드 삽입, head는 있으나 앞 노드는 없는 상태
        elif self.head != None and p == None:
            new = self.Node(name,age, None, self.head)
            self.head.pre = new
            self.head = new
        # 중간 노드 삽입
        elif p is not None:
            if p.next is not None:
                # new = self.Node(name, age, p.next.pre, p.next)
                new = self.Node(name, age, p, p.next)
                p.next.pre = new
                p.next = new
            # 마지막 노드 삽입
            else:
                p.next = self.Node(name, age, p, None)

        self.size += 1

    def delete(self, pos):
        p = self.searchNode(pos)


    def printDll(self):
        p = self.head
        i = 0
        print(f"head = {self.head}")
        while True:
            # if p.link != self.head:
            i += 1
            if p.next is not None:
                print(f"{i}. {p.name},{p.age} {p} [pre: {p.pre}, next: {p.next}] => ")
                # print(f"{p.data} => ", end="")
            else:
                print(f"{i}. {p.name},{p.age} {p} [pre: {p.pre}, next: {p.next}]")
                break
            p = p.next
        print()
