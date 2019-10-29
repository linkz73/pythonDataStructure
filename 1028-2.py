# # lambda식 : 반복문을 단축해서 사용할 때 (뒷부분에 인수 형태로 콜렉션이 옴)
# a = [1,5,4,6,8,11,3,10]
#
# # filter : 리스트를 필터링해서 일부만 반환
# even = list(filter(lambda x:(x%2==0), a))
# print(even)
#
# # map : 리스트 내의 모든 데이터에 대해 매핑
# tentimes = list(map(lambda x:x*10, a))
# print(tentimes)


# b = [[0,1,8],[7,9,3],[9,10,1],[2,3,5]]
# b.sort()
# print(b)
# # b 변수 콜렉션으로 진행하므로 인수 지정이 필요없음(lambda)
# b.sort(key=lambda x:x[2])
# print(b)



# 수행시간 체크 : 현재시간 - 시작시간
import time
import random

# seed : 시드값이 동일하면 같은 랜덤값이 나옴.
random.seed(time.time())

start_time = time.time()

a = []
for i in range(500):
    for j in range(10000):
        b = []
        b.append(random.randint(1, 1000))
    a.append(b)

print(f"--- {time.time() - start_time:.4f} seconds ---")

