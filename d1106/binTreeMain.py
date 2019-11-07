from d1106.binTree import Node, BinaryTree

t = BinaryTree()

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n8 = Node("H")

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
t.root = n1

print("Tree 의 높이 : ", t.height(t.root))
print("Tree 의 노드 갯수 : ", t.size(t.root))

u = BinaryTree()
u.root = t.copyTree(t.root)
print("T 와 U를 비교 : ", t.isEqual(t.root, u.root))
print("프리오더 : ", end='')
t.preOrder(t.root)
print()
print("인오더 : ", end='')
t.inOrder(t.root)
print()
print("포스트오더 : ", end='')
t.postOrder(t.root)
print()
print("레벨오더 : ", end='')
t.levelOrder(t.root)
print()

