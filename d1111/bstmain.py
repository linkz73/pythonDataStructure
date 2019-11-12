from d1111.bst import *

# bst 생성
t = BST()
# 노드 삽입
t.put(190,'수박')
t.put(80,'배')
t.put(70,'멜론')
t.put(50,'라임')
t.put(60,'망고')
t.put(20,'체리')
t.put(130,'포도')
t.put(35,'오렌지')
t.put(10,'귤')
t.put(15,'바나나')
t.put(45,'레몬')
t.put(40,'키위')
# inorder 출력
t.inorder(t.root)
t.put(55,'애플')
print()
t.inorder(t.root)
print()
# 노드 삭제 - 중간 노드 삭제가 난이도가 높음.
t.delete(40)
t.inorder(t.root)
# 찾기 기능
print()
print(t.get(30))
# 최소값 출력
min = t.min()
print("최소값 : ", min.key, min.value)

