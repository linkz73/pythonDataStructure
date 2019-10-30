# Single Linked List Class


class SLList:

    class Node:
        def __init__(self, name, link):
            self.name = name
            self.link = link

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertFront(self, name):
        if self.isEmpty():  # sll 이 빈상태에서 첫 노드 삽입
            # Node 클래스에 __str__ 을 따로 정의하지 않았으므로 주소를 반환하게 됨.
            self.head = self.Node(name, None)
        else:  # sll 에 기존 노드가 있는 상태에서 헤드 다음[첫 노드] 삽입
            self.head = self.Node(name, self.head)
        self.size += 1

    def insertRear(self, name, p):  # name을 p다음에 삽입
        if p is None:  # 삽입할 위치가 없는 경우, 빈 경우 -> 제일 앞 삽입
            self.insertFront(name)
        else:  # 삽입 위치가 있다.
            p.link = SLList.Node(name, p.link)
        self.size += 1

    def deleteFront(self):
        if self.isEmpty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.link
            self.size -= 1

    def deleteRear(self, p):
        if p is None:
            raise EmptyError("Underflow")
        p.link = p.link.link
        self.size -= 1

    # 해당 노드가 있는 지 여부 확인
    def search(self, trg):  
        p = self.head
        t = None
        for i in range(self.size):  # size=5 가정 0~4 반복
            if trg == p.name:
                t = i
                break
            p = p.link
        return t

    # 해당 노드의 포인터를 반환
    def searchNode(self, trg):  # Node 찾기
        p = self.head
        while p:  # size=5 가정 0~4 반복
            if trg == p.name:
                return p
            p = p.link
        return None

    def printsll(self):
        p = self.head
        # print(f"head - {p} ({self.head})")
        while p:
            if p.link is not None:
                # print(f"{p.name}-{p} ({p.link}) => ", end="")
                print(f"{p.name} => ", end="")
            else:
                print(f"{p.name}")

            p = p.link


class EmptyError(Exception):
    pass


