# binHeap
# heap 은 전 이진트리로 구성해야 함
# 리스트 : 1,2,3,4,5,6,7,8,9  (레벨오더 순서로 생각)
# i의 자노드 : 왼쪽 i * 2, 오른쪽 i*2+1
# i의 부노드 : i // 2

class BinHeap:
    def __init__(self, a):
        self.a = a  # a[0] 사용하지 않음.
        self.N = len(a) - 1  # a[0] 사용하지 않으므로

    def createHeap(self):
        for i in range(self.N // 2, 0, -1):  # range(초기값, 최종값, 증감)
            self.downHeap(i)

    def insert(self, key):
        self.N += 1   # 리스트에 추가해서 개수 증가
        self.a.append(key)
        self.upHeap(self.N)  # 마지막에 추가되었으므로 올라가면서 Heap 을 재구성
        # self.upHeap(key[0])  # 마지막에 추가되었으므로 올라가면서 Heap 을 재구성

    def deleteMin(self):  # 루트에 있는 값 삭제
        if self.N == 0:  # Heap 이 빈상태
            print("Heap이 비어 있음. 삭제 불가!!")
            return None
        mins = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]  # 첫노드와 마지막노드의 교환
        del self.a[-1]
        self.N -= 1
        self.downHeap(1)
        return mins

    def downHeap(self, i):
        while 2*i < self.N:  # i의 왼쪽 자식이 Heap에 있을 동안 반복(전이진트리이므로 좌 자노드가 없다는 것은 우 자노드도 없음)
            k = 2 * i  # k가 왼쪽 자식임을 의미.
            if k < self.N and self.a[k][0] > self.a[k+1][0]:  # 왼쪽과 오른쪽 자식을 비교
                # a[k][0] : 키값, a[k][1] : 데이터 a는 a[[], [10, 'apple'],[12,'orange'], .... ]
                k += 1  # 크다면 작은 값이 있는 쪽으로 교환
            if self.a[i][0] < self.a[k][0]:
                break

            self.a[i], self.a[k] = self.a[k], self.a[i]
            # self.a[i][0], self.a[k][0] = self.a[k][0], self.a[i][0]
            # self.a[i][1], self.a[k][1] = self.a[k][1], self.a[i][1]
            i = k  # 자식이 낮은 값이라 부모와 바뀌었으므로 k 위치에 i가 이동했으므로 i에 k값을 할당.

    def upHeap(self, i):
        while i > 1 and self.a[i//2][0] > self.a[i][0]:  # i가 1보다 크다는 것은 루트가 아니고, i 가 부모보다 작을 동안 반복
            self.a[i//2], self.a[i] = self.a[i], self.a[i//2]  # 부모와 자식의 교환
            i = i//2  # 부무와 교환되었으므로 비교위치 i를 부모로 변경

    def printHeap(self):
        print("MinHeap = ", end='')
        for i in range(1, self.N + 1):
            print('[%d:%s]' %(self.a[i][0], self.a[i][1]), end='')
        print()
        print('Heap Size: ', self.N)



