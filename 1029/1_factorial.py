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