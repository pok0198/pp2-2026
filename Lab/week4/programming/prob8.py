# 작성자 및 학번 : 황현준 / 202611852
# 작성일 : 2026 / 10 / 02
# 프로그래밍 문제 8
# printSong이라는 클래스를 작성해보자. printSong의 생성자는 노래의 가사를 리스트 형태로 받아서 객체의 내부에 저장한다. sing() 메소드는 한 줄에 한 항목씩 출력한다.

class printSong:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)

def test_prob8():
    aSong = printSong(["Twinkle, twinkle, little star,",
                       "How I wonder what you are!",
                       "Up above the world so high,",
                       "Like a diamond in the sky.",])
    aSong.sing()

if __name__ == "__main__":
    test_prob8()