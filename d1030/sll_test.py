# sll test

from d1030.sll import SLList

if __name__ == "__main__":
    s = SLList()
    s.printsll()

    s.insertFront('둘리')
    s.insertFront('도우너')
    s.insertFront('공실이')
    s.insertFront('고길동')
    s.printsll()

    p = s.searchNode("공실이")
    s.insertRear("마이콜", p)
    s.printsll()

    p = s.searchNode("둘리")
    s.insertRear("영희", p)
    s.printsll()

    s.deleteFront()
    s.printsll()

    p = s.searchNode("마이콜")
    s.deleteRear(p)
    s.printsll()

    print(f"전체 사이즈 : {s.get_size()}")