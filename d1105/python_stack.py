# infix를 입력받아 Postfix로 변환
class Postfix:
    def __init__(self):
        pass

    def is_operator(self, ch):
        if ch == '*' or ch == '/' or ch == '+' or ch == '-':
            return True
        else:
            return False

    def precedence(self, op):
        if op == '(':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 3

    def do_postfix(self, source):
        dst = []
        stack = []
        for i in source:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    t = stack.pop()
                    dst.append(t)
                stack.pop()
            elif self.is_operator(i):
                while len(stack) != 0 and self.precedence(stack[-1]) >= self.precedence(i):
                    dst.append(stack.pop())
                stack.append(i)
            elif '0' <= i <= '9':
                dst.append(i)

        while len(stack) != 0:
            t = stack.pop()
            dst.append(t)

        return(dst)


def push(item):
    stack.append(item)


def pop():
    if len(stack) != 0:
        # list의 pop 메서드는 출력하면서 삭제까지 수행
        item = stack.pop(-1)
        return item


def peak():
    if len(stack) != 0:
        return stack[-1]


def compute(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2


def eval(tokenlist):
    # tokenlist = exp.split()  # 공백을 기준으로 분할.  12 23 + : postfix = stack수식을 postfix로 표기

    for token in tokenlist:
        if token[0] in "0123456789":
            push(int(token))
        else:
            operand2 = pop()
            operand1 = pop()
            res = compute(token, operand1, operand2)
            push(res)

    return pop()


stack = []

# print("1 2 + => ", eval("1 2 +"))
expr = input("infix 수식입력 ex) (1+2)*(3-1) ==> ")
# infix => postfix 변환하는 함수
postfix = Postfix()
conv = postfix.do_postfix(expr)
print(conv)
print(expr, "=>", eval(conv))