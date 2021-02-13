from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

# text길이에 따라서 사이즈조절(여백)
btn2 = Button(root, padx=5, pady=10, text="버튼222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# 버튼사이즈고정 내용이 잘릴지라도 ㅋ.ㅋ
btn4 = Button(root, width=10, height=3, text="버튼4444444444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")  # 노란바탕에 빨간글씨
btn5.pack()

photo = PhotoImage(file="z_AI/nado/img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었어요")


# 속성삽입command '버튼이클릭되었을때 작동하라'
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
