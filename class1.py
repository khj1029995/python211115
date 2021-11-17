# class1.py

# 클래스 정의
class Person :
    # 멤버 변수(데이터 공유 목적)
    num_person = 0

    # 생성자(초기화 메소드)
    def __init__(self) :
        self.name = "defalult name"
        Person.num_person += 1 ## 클래스 차원의 데이터 공유

    def print(self) :
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p1.name = "전우치"
p2 = Person()
p1.print()
p2.print()
p3 = Person()
print("인스턴스 개수: {0}".format(Person.num_person))