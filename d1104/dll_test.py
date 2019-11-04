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

