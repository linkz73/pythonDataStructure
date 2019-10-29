# 피보나치 수열 : 피보나치
"""
0,1,1,2,3,5,8,13,21
f(n) = f(n-1) + f(n-2)
단, f(1)=0, f(2)=1

피보나치수열 활용예: 검색알고리즘
1. 선형검색(순차)
2. 제어검색
  2-1. 이분 : log2n
  2-2. 피보나치 : 데이터가 많아질수록 성능이 높아짐.
  2-3. 보간
"""


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibo_list(n):
    lst = list()
    for i in range(n):
        lst.append(str(fibo(i)))
    return lst

indata = int(input('피보나치 수열 갯수 입력 : '))
print(f"피보나치 {indata} -> {', '.join(fibo_list(indata))}")

f = []
def fibo1(n):
    for i in range(n):
        if i == 0:
            f.append(0)
        elif i == 1:
            f.append(1)
        else:
            f.append(f[i-1] + f[i-2])


indata1 = int(input('피보나치 수열 갯수 입력 : '))
print(f"피보나치 {indata1} -> {fibo1(indata1)}")