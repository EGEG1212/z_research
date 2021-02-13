from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 여러줄입력
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")  # 힌트텍스트

# 한줄입력
e = Entry(root, width=30)  # 한줄입력 (엔터키안먹음)
e.pack()
e.insert(END, "한 줄만 입력가능합니다")  # 현재는 값이 비어있으므로 END를 써도 됨. 0인덱스넣어줌


def btncmd():
    # 내용출력
    print(txt.get("1.0", END))  # 텍스트 라인1.컬럼0부터 끝까지 가져와서 프린트
    print(e.get())

    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
