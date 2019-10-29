"""
재귀적 호출 : Recursive Call : 가급적 쓰지 않는 것이 좋다. (해당 함수가 복사되서 메모리 차지함. 가급적 함수 크기를 작게)
a -> a, a->b->a
어쩔수 없이 사용해야 하는 경우
예) 팩토리얼, 피보나치 수열, 이진트리 운행(윈도탐색기 검색의 기본 원리)
주의 : 반드시 내부에 종료 조건을 포함
"""

# factorial 함수 재귀적 호출의 예

# def fact(n):
#     if n <= 1:  #재귀적 호출의 종료조건
#         return 1
#     else:
#         return n * fact(n-1)  #재귀적 호출
#
# indata = int(input("숫자 입력 : "))
# print("fact(%d) = " %(indata), fact(indata))

# factorial 의 반복문예
def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i

    return res

indata = int(input("숫자 입력 : "))
print("fact(%d) = " %(indata), fact(indata))


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