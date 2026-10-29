import tkinter as tk                                                                    # 모듈 불러오기

root = tk.Tk()                                                                          # 창(윈도우) 생성

root.title("Oobutton")                                                                  # 타이틀 제목 설정
root.geometry("600x400")                                                                # 창(윈도우) 크기 설정

def on_label_clicked(event):                                                            # 라벨 클릭 함수 설정 및 이벤트로 정의
    print(f"라벨이 클릭되었습니다 : {event}")                                             # 버튼 출력 텍스트 정의(이벤트)

label = tk.Label(root, text = "객체지향 윈도우 프로그래밍")                                # 라벨 생성 및 텍스트 설정
label.bind("<Double-1>", on_label_clicked)                                              # 라벨 바인드 생성
label.pack()                                                                            # 레이블 패키징

def on_btn1_clicked(event):                                                                  # 버튼 클릭 함수 설정 및 이벤트로 정의
    print(f"버튼이 클릭되었습니다. {event}")                                                         # 버튼 출력 텍스트 정의(이벤트)
    label.config(text = f"버튼1이 클릭되었습니다.{event}")

#btn1 = tk.Button(root, text = "클릭해볼까요?", command= on_btn1_clicked)                 # 버튼 생성 및 텍스트 설정
btn1 = tk.Button(root, text = "클릭해볼까요?", width = 100, height = 50, fg = "red", bg = "black")      # 버튼 생성 및 텍스트 설정, 크기 설정, 색 설정, 백그라운드 색 설정
btn1.bind("<Button-1>", on_btn1_clicked)                                               # 버튼 바인드 생성
btn1.pack()                                                                             # 버튼 패키징



root.mainloop()                                                                          # 사용자가 동작할때까지 대기