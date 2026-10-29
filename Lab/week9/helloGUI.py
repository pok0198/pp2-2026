#from tkinter import *                           # tkinter모듈 불러오기
import tkinter as tk                            # 이렇게 작성 가능 단 앞에 tk.을 붙어야 됨

window = tk.Tk()                                   # 창(윈도우) 생성
window.title("Hello 황현준")                    # 창(윈도우)의 타이틀 저장
window.geometry("400x200")                      # 창(윈도우)의 크기 설정

label = tk.Label(window, text="Hello GUI!")     # 위젯 생성 및 텍스트 저장
label.pack()                                    # 위젯을 창(윈도우)에 배치

window.mainloop()                               # 창(윈도우)이 사용자 동작을 대기