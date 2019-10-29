# 학생 Class 생성
# 멤버 변수 [속성]  private 형태(self)  _name, id
# getter(멤버변수 값 -> 외부): _name, id
# setter(멤버변수 값 <- 외부) : _name


class Student:
    def __init__(self, name, id=10):  # 생성자, 초기변수와 객체 생성시 초기값 설정.
        self._name = name
        self.id = id

    def get_name(self):  # 멤버 변수값 -> 외부
        return self._name

    def get_id(self):
        return self.id

    def set_name(self, name):  # 멤버 변수값 <- 외부
        self._name = name

    # 오버라이딩 : 객체지향 프로그래밍. 상속, 부모의 함수를 자식에서 변경해서 사용.
    # 오버로딩 : 동일 기능이지만 매개면수의 형식 차이 - 파이썬은 자체 지원하므로 따로 만들지 않음.
    def __str__(self):  # 오버라이딩한 특수 메소드 : 객체명을 출력에 이용할 경우 사용
        return self._name + ", " + str(self.id)


if __name__ == '__main__':
    s1 = Student('Nam', 100)  # 객체변수  = 클래스명(생성ㅈ에 필요한 매개면수)
    # s1.id = 200
    # print(s1._name) 지양
    print(s1.get_name())
    s1.set_name('Kim')
    print(s1)

    s2 = Student('Kim')
    print(s2.get_id())

    # my_student = Student('Nam', 10)
    # print(f"my_student.get_name() is {my_student.get_name()}")
    # print(f"my_student.get_id() is {my_student.get_id()}")


