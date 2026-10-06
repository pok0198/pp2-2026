# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 4
# 사각형을 나타내는 Rectangle 클래스를 작성하여 보자. Rectangle 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f"({self.x}, {self.y}, {self.w}, {self.h})"

    def getArea(self):
        return self.w * self.h
    
    def overlap(r1, r2):
        if (
            r1.getArea() == r2.getArea()
        ):
            print(f"r1과 r2는 서로 겹칩니다")
        else:
            print(f"r1과 r2는 서로 겹치지 않습니다.")

def test_prob4():

    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    r1.overlap(r2)

if __name__ == "__main__":
    test_prob4()

#    def setX(self, x):
#        self.x = x

#    def setY(self, y):
#        self.y = y

#    def setW(self, w):
#        self.w = w

#    def setH(self, h):
#        self.h = h

#    def getX(self):
#        return self.x

#    def getY(self):
#        return self.y

#    def getW(self): 
#        return self.w

#    def getH(self):
#        return self.h