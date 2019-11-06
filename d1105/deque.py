from collections import deque

dq = deque('data'"kkk""")
for node in dq:
    print(node.upper(), end='')

print()

dq.append('aaa')
dq.appendleft('bbb')
dq.append('bbb')
dq.append('ccc')
print(dq)


print('deque =>', dq.pop)
print('deque =>', dq.popleft())
print('deque =>', dq[-1])
print('deque =>', dq[2])
print('deque =>', dq[0])
print(dq)

print('t' in dq)
# 문자를 한자씩 끊어서 입력함
dq.extend('deque')
print(dq)
dq.extendleft(reversed('python'))

print(dq)
dq.reverse()
print(dq)