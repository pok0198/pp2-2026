# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 3
# 상자를 나타내는 Box 클래스를 작서아여보자. Box 클래스는 가로길이, 세로길이, 높이를 나타내는 인스턴스 변수를 가진다.

class Box:
    def __init__(self, length, height, depth):
        self.length = length
        self.height = height
        self.depth = depth

    def __str__(self):
        return f"({self.length},  {self.height}, {self.depth})"
    
    def getlength(self):
        return self.length

    def getheight(self):
        return self.height

    def getdepth(self):
        return self.depth

def test_prob3():
    b1 = Box(100, 100, 100)
    print(b1)
    print("상자의 부피는 : ", b1.getlength() * b1.getheight() * b1.getdepth())

if __name__ == "__main__":
    test_prob3()