

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
        # 하나 남은 노드 삭제
        if p.pre is None and p.next is None:
            self.head = None

        # 첫 노드 삭제
        elif p.pre is None:
            p.next.pre = None
            self.head = p.next

        # 마지막 노드 삭제
        elif p.next is None:
            p.pre.next = None

        # 중간 노드 삭제
        # elif not(p.pre is None or p.next is None):
        else:
            # elif p.pre is not None and p.next is not None:
            p.pre.next = p.next
            p.next.pre = p.pre

        self.size -= 1

    def printDll(self):
        p = self.head
        i = 0
        # print(f"head = {self.head}")
        while True:
            # if p.link != self.head:
            i += 1
            # if p is None:
            if self.isEmpty():
                print("링크드리스트 비어 있음")
                break
            else:
                if p.next is not None:
                    # print(f"{i}. {p.name},{p.age} {p} [pre: {p.pre}, next: {p.next}] => ")
                    print(f"{i}. {p.name},{p.age}  => ", end="")
                    # print(f"{p.data} => ", end="")
                else:
                    # print(f"{i}. {p.name},{p.age} {p} [pre: {p.pre}, next: {p.next}]")
                    print(f"{i}. {p.name},{p.age}")
                    break
            p = p.next
