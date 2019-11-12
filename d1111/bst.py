# Binary Search Tree : 검색 트리

class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # 검색기능
    def get(self, k):
        return self.getItem(self.root, k)

    def getItem(self, n, k):
        if n is None:  # 빈상태
            return None

        if n.key > k:
            return self.getItem(n.left, k)
        elif n.key < k:
            return self.getItem(n.right, k)
        else:  # n.key == k 찾은 경우
            return n.value

    # 노드 삽입
    def put(self, key, value):
        self.root = self.putItem(self.root, key, value)

    def putItem(self, n, k, v):
        if n is None:
            return Node(k, v)

        if n.key > k:
            n.left = self.putItem(n.left, k, v)
        elif n.key < k:
            n.right = self.putItem(n.right, k, v)
        else:  # n.key == k 같은 노드가 존재하는 경우. 삽입 불가/갱신
            n.value = v
        return n

    # 메뉴 만들때 전체에서 최소값 삭제시 필요    
    def deleteMin(self):  # root 부터 최소값 삭제
        if self.root is None:
            print("트리가 비어 있음")
        self.root = self.delMin(self.root)

    # 특정노드 아래에서 최소값 삭제
    def delMin(self, n):  # 특정 노드부터 최소값 찾기
        if n.left is None:
            return n.right
        n.left = self.delMin(n.left)
        return n

    def min(self):  # 최소값 찾기
        if self.root is None:
            return None

        return self.minimum(self.root)

    def minimum(self, n):
        if n.left is None:
            return n

        return self.minimum(n.left)

    def inorder(self, n):
        if n is not None:
            if n.left:
                self.inorder(n.left)
            print(f"[{str(n.key)} {n.value}]", end='')
            if n.right:
                self.inorder(n.right)

    # 메뉴에서 특정 노드 삭제
    def delete(self, k):
        self.root = self.delNode(self.root, k)

    def delNode(self, n, k):
        if n is None:  # 비어 있어 삭제 못함
            return None
        if n.key > k:
            n.left = self.delNode(n.left, k)
        elif n.key < k:
            n.right = self.delNode(n.right, k)
        else:  # 삭제할 노드를 찾은 경우
            # 1. 오른쪽 자노드가 없거나 자노드가 없는 경우
            if n.right is None:
                return n.left
            # 2. 왼쪽 자노드가 없는 경우,
            if n.left is None:
                return n.right
            # 3.자노드가 2개 중 오른 쪽의 최소값을 삭제된 노드로 대체
            t = n
            n = self.minimum(t.right)
            n.right = self.deleteMin(t.right)
            n.left = t.left
            # n = self.maximum(t.left)
            # n.left = self.deleteMax(t.left)
            # n.right = t.right
        return n
    #
    #
    # def max(self):
    #     if self.root is None:
    #         return None
    #
    #     return self.minimum(self.root)
    #
    # def maximum(self, n):
    #     if n.right is None:
    #         return n

    # def deleteMax(self):  # 최댓값 삭제
    #     if self.root is None:
    #         print("BST가 비었음")
    #         return None
    #     self.root = self.delMax(self.root)
    #
    # def delMax(self, n):
    #     if n.right is None:
    #         return n.left
    #     n.right = self.delMax(n.right)
    #     return n







