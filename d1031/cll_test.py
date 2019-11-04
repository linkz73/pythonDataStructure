# sll test

from d1031.cll import CLList

if __name__ == "__main__":
    cll = CLList()
    cll.printcll()

    cll.insertFront('둘리')
    cll.insertFront('도우너')
    cll.insertFront('공실이')
    cll.insertFront('고길동')
    cll.printcll()

    p = cll.searchNode("공실이")
    cll.insertRear("마이콜", p)
    cll.printcll()
    print(f"전체 사이즈 : {cll.get_size()}")

    p = cll.searchNode("둘리")
    cll.insertRear("또치", p)
    cll.printcll()

    # p = cll.searchNode("철수")
    # cll.insertRear("또치1", p)
    # cll.printcll()

    # cll.deleteFront()
    # cll.printcll()
    #
    # p = cll.searchNode("공실이")
    # cll.deleteRear(p)
    # cll.printcll()
    #
    # p = cll.searchNode("고길동")
    # cll.deleteRear(p)
    # cll.printcll()

    print(f"cll.head : {cll.head}")
    print(f"cll.head.link : {cll.head.link}")
    print(f"cll.tail : {cll.tail}")
    print(f"cll.tail.link : {cll.tail.link}")

