# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 2
# 로켓을 나타내는 Rocket 클래스를 작성해보자, Rocket 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.

class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def moveUP(self):
        self.y += 1

    def __str__(self):
        return f"{self.y}"
    
def test_prob2():
    myRocket = Rocket(0, 0)     
    print("로켓의 높이 : ", myRocket.y)

    myRocket.moveUP()
    print("로켓의 높이 : ", myRocket.y)

if __name__ == "__main__":
    test_prob2()