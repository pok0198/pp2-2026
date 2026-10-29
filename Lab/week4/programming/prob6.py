# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 6
# Person이라는 클래스를 작성해보자. Person 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.

class Person:
    def __init__(self, n, m, o, e):
        self.name = n
        self.mobile = m
        self.office = o
        self.email = e

    def __str__(self):
        return f"{self.name}, {self.mobile}, {self.office}, {self.email}"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMobile(self, mobile):
        self.mobile = mobile

    def getMobile(self):
        return self.mobile

    def setOffice(self, office):
        self.office = office

    def getOffice(self):
        return self.office

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email


def test_prob6():
    p1 = Person("Kim", "010-1234-5678", "1234567", "kim@company.com")
    p2 = Person("Park", "010-2345-6789", "2345678", "park@company.com")

    print(p1)
    print(p2)

    p2.setEmail("park2@company.com")
    print(p2.getEmail())


if __name__ == "__main__":
    test_prob6()