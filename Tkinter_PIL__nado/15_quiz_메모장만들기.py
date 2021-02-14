import os
from tkinter import *

root = Tk()
root.title("Windows 메모장")
root.geometry("640x480")

# 열기, 저장 파일이름
filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)  # 텍스트위젯 본문삭제하고
            txt.insert(END, file.read())  # 뒤에 파일내용을 본문에 입력


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))  # 모든내용을 가져와서 저장


menu = Menu(root)

# File메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)  # 창꺼짐
menu.add_cascade(label="파일", menu=menu_file)

# 그 외 메뉴(빈값)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 메모장본문영역 scrollbar와 txt가 서로가 서로를 바라보게? 맵핑
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

# scrollbar와 txt가 서로가 서로를 바라보게? 맵핑
scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
