# Circular Linked List

class CLList:

    class Node:
        def __init__(self, data, link):
            self.data = data
            self.link = link

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insertFront(self, data):
        if self.isEmpty():
            t = self.Node(data, None)  # 빈 노드의 주소
            self.head = t  # 빈노드를 헤드로 지정
            self.head.link = t  # 빈노드 주소를 헤드가 가리키는 링크에 입력
            self.tail = t  # 헤드의 주소를 tail 이 가리키는 링크에 입력
        else:
            # head 주소값을 받아와 노드를 만들고 그 노드의 주소를 헤드에 입력
            self.head = self.Node(data, self.head)
            self.tail.link = self.head

        self.size += 1

    def insertRear(self, data, p):
        if p is None:
            self.insertFront(data)
        elif p.link != self.head:
            # p 위치의 주소를 노드에 입력하고 이 노드의 주소를 원래의 p.link 에 주소를 대체하면 뒤쪽 삽입이 완료
            # 기존 sll 과 동일
            p.link = CLList.Node(data, p.link)
        else:  # 마지막 노드
            self.tail = self.tail.link = CLList.Node(data, self.head)

        self.size += 1

    def deleteFront(self):
        if self.isEmpty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.link
            self.tail.link = self.head

            self.size -= 1

    def deleteRear(self, p):
        if self.isEmpty() or p is None:
            raise EmptyError("Underflow")
        elif p != self.tail:  # 중간
            p.link = p.link.link
        elif p == self.head:  # 처음
            self.deleteFront()
        elif self.head == self.tail: # 삭제할 노드가 한개
            self.head = self.tail = None
        else:  # 마지막 노드
            p.link = p.link.link
            self.tail = p
            self.tail.link = self.head

        self.size -= 1

    # 해당 노드가 있는 지 여부 확인
    def search(self, trg):
        p = self.head
        t = None
        for i in range(self.size):  # size=5 가정 0~4 반복
            if trg == p.data:
                t = i
                break
            p = p.link
        return t

    # 해당 노드의 포인터를 반환
    def searchNode(self, trg):  # Node 찾기
        p = self.head
        # while p != self.tail:  # size=5 가정 0~4 반복
        #     if trg == p.data:
        #         return p
        #     p = p.link
        #
        # if p == self.tail and trg == p.data:
        #     return p
        #
        # return None

        while True:
            if trg == p.data:
                return p
            if p.link == self.head:
                return None
            p = p.link

    def printcll(self):
        p = self.head
        # print()
        # print(f"head - {self.head} [link : {self.head.link}]")
        # print(f"tail - {self.tail} [link : {self.tail.link}]")
        while p:
            if p.link != self.head:
                # print(f"{i}.{p.data}-{p} [link : {p.link}] => ", end="")
                print(f"{p.data} => ", end="")
            else:
                print(f"{p.data}")
                break
            p = p.link

class EmptyError(Exception):
    pass