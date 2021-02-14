import time
import keyboard  # pip install keyboard
from PIL import ImageGrab  # 파이썬이미지라이브러리 pip install Pillow


def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()  # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # 사용자가 F9키를 누르면 스크린샷저장

keyboard.wait("esc")  # 사용자가 esc를 누를 때까지 프로그램수행
