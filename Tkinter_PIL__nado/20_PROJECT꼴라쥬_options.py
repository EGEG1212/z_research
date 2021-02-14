import os
import tkinter.ttk as ttk  # Combobox, ProgressBar를위해
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog  # 기능파일추가를위해
from PIL import Image  # 이미지통합할때

root = Tk()
root.title("Nado GUI")


def merge_image():  # 이미지 통합
    # 옵션받아오기-1.가로넓이
    img_width = cmb_width.get()
    if img_width == "원본유지":
        img_width = -1  # -1일때는원본기준으로
    else:
        img_width = int(img_width)

    # 옵션받아오기-2.간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 60
    elif img_space == "넓게":
        img_space = 90
    else:  # 없음
        img_space = 0

    # 옵션받아오기-3.포맷
    img_format = cmb_format.get().lower()  # PNG,JPG,BMP값을 받아와서 소문자로 변경
    ##############################

    print(list_file.get(0, END))  # 모든 파일 목록을 가지고 오기
    images = [Image.open(x) for x in list_file.get(0, END)]
    # 이미지 사이즈 리스트에 넣어서 하나씩 처리
    image_sizes = []
    if img_width > -1:  # -1이면 원본유지니까 그보다 크면
        # width값변경
        image_sizes = [(int(img_width), int(
            img_width * x.size[1] / x.size[0])) for x in images]
    else:  # -1이면 원본사이즈적용
        image_sizes = [(x.size[0], x.size[1]) for x in images]
    # size-> size[0]:width, size[1]:height
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images] #요두줄을 아래 한줄로 만듦 unzip??
    # widths, heights = zip(*(x.size for x in images)) #이 한줄을 아래옵션넣은 image_sizes를 적용하여 변경
    widths, heights = zip(*(image_sizes))

    # 최대넓이, 전체높이 구하기(스케치북준비하려고)
    max_width, total_height = max(widths), sum(heights)
    print("max width : ", max_width)
    print("total height : ", total_height)
    # 스케치북준비
    if img_space > 0:  # 이미지 간격 옵션 적용
        total_height += (img_space * (len(images) - 1))
    result_img = Image.new(
        "RGB", (max_width, total_height), (255, 255, 255))  # 배경흰색
    y_offset = 0  # y기준으로 이미지위치잡기
    # for img in images:
    #     result_img.paste(img, (0, y_offset))
    #     y_offset += img.size[1]  # height값 만큼 더해줌.....여기까지3줄 pogress bar연동을위해 코멘트처리
    for idx, img in enumerate(images):
        # width가 원본유지가 아닐때에는 이미지 크기 조정
        if img_width > -1:
            img = img.resize(image_sizes[idx])  # 옵션적용된image_sizes값으로 resize

        result_img.paste(img, (0, y_offset))
        y_offset += (img.size[1] + img_space)  # height값 + 사용자가지정한간격
        progress = (idx+1) / len(images) * 100  # 실제 %정보를 계산(인덱스가0부터시작하니까+1)
        p_var.set(progress)
        progress_bar.update()

    # 포맷옵션처리
    file_name = "nado_photo." + img_format
    # 결과물저장경로
    dest_path = os.path.join(txt_dest_path.get(), file_name)
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다.")


def add_file():  # 기능-파일추가:복수개의 파일선택가능 askopenfilenames
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(
        ("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir=r"C:\Users\pc-go\WORKSPACE")
    # 사용자가 선택한 파일 목록
    for file in files:
        # print(file)
        list_file.insert(END, file)


def del_file():  # 기능-파일선택삭제:인덱스가바뀌니까 뒤에서부터 삭제해야함
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def browse_dest_path():  # 기능-저장경로(폴더)
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # 만약사용자가 [취소]눌러서 저장경로가 없을때
        return
    print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)  # 선택한경로가 들어가게


def start():
    # r각 옵션들 값을 확인
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일목록확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    # 저장경로확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 통합작업
    merge_image()


# 파일 프레임(파일추가, 선택삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)  # 프레임간의 간격띄우기

btn_add_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임(리스트박스&스크롤바)
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)  # 프레임간의 간격띄우기

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)  # 프레임간의 간격띄우기

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,
                   padx=5, pady=5, ipady=4)  # 안쪽패딩ipad높이

btn_dest_path = Button(path_frame, text="찾아보기",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)  # 프레임간의 간격띄우기

#  1.가로넓이옵션
#     가로넓이레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)
#     가로넓이콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

#  2.간격옵션
#     간격옵션레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)
#     간격옵션콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

#  3.파일포맷옵션
#     파일포맷옵션레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
#     파일포맷옵션콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly",
                          values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행상황Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)  # 프레임간의 간격띄우기

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)  # 프레임간의 간격띄우기

btn_close = Button(frame_run, padx=5, pady=5, text="닫기",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start = Button(frame_run, padx=5, pady=5,
                   text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)  # x너비 y높이 값 변경불가(창크기변경불가)
root.mainloop()
