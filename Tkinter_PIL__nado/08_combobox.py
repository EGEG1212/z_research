import tkinter.ttk as ttk  # 콤보박스쓰려면 꼭 선언해야함
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 1~31까지의 숫자 i for i in range(1, 32)
values = [str(i) + "일" for i in range(1, 32)]
# 단점은 글자입력을 해버릴수있음; 선택만하라고!!!!
combobox = ttk.Combobox(root, height=5, values=values)  # height는 목록의 갯수
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(
    root, height=10, values=values, state="readonly")  # 선택만가능하게state="readonly"
readonly_combobox.current(0)  # 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()
