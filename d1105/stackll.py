class Node:
    def __init__(self, item, link):
        self.item = item
        self.link = link


    
    

def push(item):
    global top, size
    top = Node(item, top)
    # if max <= size:
    #     print("overflow")
    #     return
    size += 1


def get_size():
    return size


def pop():
    global top, size
    if size != 0:
        top_item = top.item
        top = top.link
        size -= 1
        return top_item
    else:
        print("Underflow 발생")
        
        
def peak():
    if size != 0:
        print(top.item)
    else:
        print("Underflow 발생, 없음")
    # return None 결과가 나오는 경우도 있음. 확인 필요


def printStack():
    print("Top ->\t", end="")
    p = top
    while p:
        if p.link is not None:
            print(p.item, " -> ", end="")
        else:
            print(p.item)

        p = p.link


top = None
size = 0
# max = 10  # push 시 오버플로를 검증하기 위해 필요
