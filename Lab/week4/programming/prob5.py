# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 5
# 삼각형을 나타내는 클래스 Triangle을 작성해보자. Triangle 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.

class Triangle:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        numberofSides = 3

    def checkAngles(self):
        if self.a1 + self.a2 + self.a3 == 180:
            return "내각의 합이 180도입니다."
        else:
            return "내각의 합이 180도가 아닙니다."

    def __str__(self):
        return f"{self.a1}+{self.a2}+{self.a3}"

def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())

if __name__ == "__main__":
    test_prob5()