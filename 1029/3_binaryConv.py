# 10진수를 입력받아 2진수로 출력하는 함수를 재귀적 호출 작성

# 재귀적 호출시 출력을 마지막부터 하려면 함수 호출 후 출력 구문을 삽입하면 됨.

def dec2bin(n):
    if n == 0:
        return

    dec2bin(n//2)
    print(n % 2, end='')
    return

indata = int(input("십진수 입력 : "))
print(f"십진수 : {indata} -> 이진수: ")
dec2bin(indata)