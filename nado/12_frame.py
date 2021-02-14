from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

# 메뉴프레임
frame_burger = Frame(root, relief="solid",
                     bd=1)  # 테두리 relief="solid"
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()  # 프레임안에 버튼넣음
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료프레임
frame_drink = LabelFrame(root, text="음료")  # LabelFrame이라 text="음료"로 제목달기
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()
