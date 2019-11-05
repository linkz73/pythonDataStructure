from d1104.dll import DLList

if __name__ == "__main__":
    dll = DLList()

    dll.insert("철수", 12)
    dll.printDll()

    dll.insert("영희", 11)
    dll.printDll()

    dll.insert("길동", 40, "철수")
    dll.printDll()

    dll.insert("둘리", 7, "영희")
    dll.printDll()

    print(f"전체 크기 : {dll.get_size()}")

    dll.delete('영희')
    dll.printDll()

    dll.delete('철수')
    dll.printDll()

    dll.delete('길동')
    dll.printDll()

    dll.delete('둘리')
    dll.printDll()

