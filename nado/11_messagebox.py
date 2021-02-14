import tkinter.messagebox as msgbox  # 메시지박스 이거 선언해야함
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 기차 예매 시스템으로 가정


def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")


def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")


def error():
    msgbox.showwarning("에러", "결제 오류가 발생했습니다.")


def okcancel():
    # 사용자에게 ok누를껀지 cancel누를껀지 물어보는것[확인][취소]
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")


def retrycancel():
    # 사용자에게 [다시시도][취소] 뭐 누르겠느냐~~
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1:  # 재시도, ok
        print("재시도")
    elif response == 0:  # 취소
        print("취소")


def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")


def yesnocancel():  # 타이틀없이팝업/ [예]저장하고종료 [아니요]저장없이종료 [취소]프로그램종료취소(현재화면에서 계속작업)
    response = msgbox.askyesnocancel(
        title=None, message="예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 종료하시겠습니까?")
    print("응답:", response)  # True예1, False아니오0, None그외
    if response == 1:  # 네, ok
        print("예")
    elif response == 0:  # 아니오
        print("아니오")
    else:
        print("취소")


#command=함수명, 버튼에표기되는text
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()
