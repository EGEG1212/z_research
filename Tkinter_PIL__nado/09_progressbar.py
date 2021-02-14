import time
import tkinter.ttk as ttk  # 콤보박스,프로그레스바 쓰려면 꼭 선언해야함
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar.start(10)  # 10ms마다 움직임(1은 넘나빠름ㅋ). 위에서 mode가 indeterminate정해지지않아서 좌우로 움직임; 언제끝날지모름
# -
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 10ms마다 움직임(1은 넘나빠름ㅋ). determinate뭔가 차오르는 느낌!
# progressbar.pack()


# def btncmd():
#     progressbar.stop()  # 작동중지.. 그런데 초록바마저 확 사라져버림; 이게 뭐야 ㅋㅋㅋㅋㅋ

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()  # 플롯속도도 실수로반영하기위해 더블바
progressbar2 = ttk.Progressbar(
    root, maximum=100, length=150, variable=p_var2)  # length가로바 길이가 좀 길어짐
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var2.set(i)
        progressbar2.update()  # ui업데이트를 안하면 한방에 뽷; 업데이트를해야 주우욱커짐
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop()
