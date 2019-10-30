# sll Menu

from d1030.sll import SLList


def menu():
    print()
    print("======== MENU ========")
    print("1. 앞에 삽입")
    print("2. 뒤에 삽입")
    print("3. 처음 삭제")
    print("4. 선택 삭제")
    print("5. 검색")
    print("6. 목록 보기")
    print("0. 종료")


if __name__ == "__main__":
    s = SLList()

    while True:
        menu()
        sel = input("menu select : ")

        if sel == "1":
            data = input("삽입할 데이터 입력 : ")
            s.insertFront(data)
            s.printsll()

        elif sel == "2":
            data = input("삽입할 데이터 입력 : ")
            pos = input("삽입할 위치 입력 : ")
            p = s.searchNode(pos)
            s.insertRear(data, p)
            s.printsll()

        elif sel == "3":
            s.deleteFront()
            s.printsll()

        elif sel == "4":
            pos = input("삭제할 앞의 위치 입력 : ")
            p = s.searchNode(pos)
            s.deleteRear(p)
            s.printsll()

        elif sel == "5":
            data = input("검색할 값 입력 : ")
            pos = s.search(data)
            print(f"검색어 {data}의 전체 위치는 앞에서 {pos + 1} 번째 입니다.")

        elif sel == "6":
            print("목록 결과 : ")
            s.printsll()

        elif sel == "0":
            print("사용 종료")
            break

        else:
            print("선택실패 다시 선택하시오.")