# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 9
# 터틀 그래픽에서 각각의 거북이는 객체이다. 2개의 거북이를 생성하여서 다음과 같이 서로다른 방향으로 움직이도록 하자.

import turtle


def test_prob9():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()

    t1.goto(100, 0)
    t1.goto(100, -100)
    t1.goto(300, -100)

    t2.goto(-100, 0)
    t2.goto(-100, 100)
    t2.goto(-300, 100)

    turtle.done()


if __name__ == "__main__":
    test_prob9()