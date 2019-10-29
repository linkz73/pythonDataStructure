
# 자료구조
# - 선형구조 : 연접리스트(리스트, 배열), 연결리스트(스택, 큐, 덱)
# - 비선형구조 : 트리, 그래프

# 이진트리-운행법
# pre-order : 앞 이마
# in-order : 가랑이
# post-order : 뒷 이마
# ** 수식일 경우는 fix 로 표현
# 노드 들 중에 제일 아래 자노드가 없는 노드를 단노드라고 함

class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def map():
    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")
    n4 = Node("D")
    n5 = Node("E")
    n6 = Node("F")
    n7 = Node("G")
    n8 = Node("H")
    n9 = Node("I")
    n10 = Node("J")
    n11 = Node("K")
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.left = n10
    n5.right = n11
    return n1


def preOrder(n):
    if n is not None:
        print(n.name, '=>', end="")
        preOrder(n.left)
        preOrder(n.right)

def postOrder(n):
    if n is not None:
        postOrder(n.left)
        postOrder(n.right)
        print(n.name, '=>', end="")

def inOrder(n):
    if n is not None:
        inOrder(n.left)
        print(n.name, '=>', end="")
        inOrder(n.right)

start = map()
print(type(start))
print("inOrder : \t", end="")
inOrder(start)
print()
print("preOrder : \t", end="")
preOrder(start)
print()
print("postOrder : \t", end="")
postOrder(start)

# 재귀적 호출 : Recursive Call : 가급적 쓰지 않는 것이 좋다. (해당 함수가 복사되서 메모리 차지함. 가급적 함수 크기를 작게)
# a -> a, a->b->a
# 어쩔수 없이 사용해야 하는 경우
# 예) 팩토리얼, 피보나치 수열, 이진트리 운행(윈도탐색기 검색의 기본 원리)
# 주의 : 반드시 내부에 종료 조건을 포함
