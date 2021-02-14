from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 스크롤바, 위젯을 하나의 프레임에 넣어야 관리가 편함
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")  # 스크롤바 세로로 길게 fill

# set이없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)  # listbox에 scrollbar를 담았고(1)
for i in range(1, 32):  # 1~31일
    listbox.insert(END, str(i) + "일")  # 1일,2일...
listbox.pack(side="left")

# scrollbar에 listbox를 담아서(2) 서로가 서로를 바라보게? 맵핑
scrollbar.config(command=listbox.yview)

root.mainloop()
