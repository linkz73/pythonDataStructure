# getter, setter 다른 예제

class Student:
    def __init__(self, name, id=10):
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @id.setter
    def id(self, new_id):
        self.__id = new_id


if __name__ == '__main__':
    s1 = Student('Kim', 10)
    print(s1.name)
    s1.name = "Nam"
    s1.id = 100
    print(f"@property 와 @~~.setter 를 활용한 예제 / name : {s1.name} and id : {s1.id}")


