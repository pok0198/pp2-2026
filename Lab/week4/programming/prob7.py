# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 7
# 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성해보자. PhoneBook 클래스는 딕셔너리를 이용하여서 연락처를 저장한다.

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "mobile": mobile,
            "office": office,
            "email": email
        }

    def __str__(self):
        return f"{self.contacts}"

def test_prob7():
    obj = PhoneBook()
    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")
    print(obj)

if __name__ == "__main__":
    test_prob7()