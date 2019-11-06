# 이진트리 만들기
# 이진트리의 Null link(none) 갯수는 (노드 갯수 + 1)


class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    # pre : 출력 왼쪽 오른쪽 / post : 왼쪽 오른쪽 출력 / in-order : 왼쪽 출력 오른쪽

    def preOrder(self, n):
        if n is not None:
            print(str(n.item), ' ', end='')
            if n.left is not None:
                self.preOrder(n.left)
            if n.right is not None:
                self.preOrder(n.right)

    def inOrder(self, n):
        if n is not None:
            if n.left is not None:
                self.inOrder(n.left)
            print(str(n.item), ' ', end='')
            if n.right is not None:
                self.inOrder(n.right)

    def postOrder(self, n):
        if n is not None:
            if n.left is not None:
                self.postOrder(n.left)
            if n.right is not None:
                self.postOrder(n.right)
            print(str(n.item), ' ', end='')

    def levelOrder(self, root):
        q = list()
        q.append(root)
        while len(q) != 0:  # q 가 비어 있지 않을 동안 반복
            t = q.pop(0)
            print(str(t.item), ' ', end='')
            if t.left is not None:
                q.append(t.left)
            if t.right is not None:
                q.append(t.right)

    def height(self, root):  # depth, 재귀호출 사용
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left) + self.height(root.right)) 
        
    def size(self, root):  # 재귀호출 사용해 전체 노드수 구하기
        if root is None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)

    def copyTree(self, n):  # 재귀호출
        if n is None:
            return None
        else:
            left = self.copyTree(n.left)
            right = self.copyTree(n.right)
            return Node(n.item, left, right)

    def isEqual(self, n, m):  # 재귀 호출
        if n is None and m is None:
            return n == m
        if n.item != m.item:
            return False
        # else:
        #     return True
        return (self.isEqual(n.left, m.left)) and (self.isEqual(n.right, m.right))

    # 데이터는 강제 삽입


