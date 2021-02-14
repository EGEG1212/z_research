from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended",
                  height=0)  # extended다중선택, single한개선택 / height=0리스트전체보여줌,3이면 3줄만보여주고 내려서봐야함.스크롤바는 따로만들어야함
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # listbox.delete(END)  # 클릭버튼을 누르면 제일 끝부터 삭제됨
    # listbox.delete(0) # 클릭버튼을 누르면 제일 앞부터 삭제됨

    # 갯수확인
    print("리스트에는", listbox.size(), "개가 있어요")

    # 항목확인(시작인덱스, 끝인덱스)
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 인덱스 확인
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
