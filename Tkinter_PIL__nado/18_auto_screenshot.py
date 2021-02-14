import time
from PIL import ImageGrab  # 파이썬이미지라이브러리 pip install Pillow

time.sleep(5)

for i in range(1, 11):  # 2초간격으로 10개 이미지 저장
    img = ImageGrab.grab()  # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i))
    time.sleep(2)
