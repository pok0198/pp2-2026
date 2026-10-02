# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 1번 
# 고양이를 클래스로 정의하고 몇 개의 인스턴스를 생성해보자. 접근자와 설정자를 사용해보자.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):      # str 메소드 사용법을 더 익히기
        return f"{self.name} {self.age}"

def test_prob1():
    missy = Cat("Missy", 3)
    lucky = Cat("Lucky", 5)
    print(missy)
    print(lucky)

if __name__ == "__main__":
    test_prob1()