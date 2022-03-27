# 이미지에서 텍스트추출하기
# https://devsmile.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%97%90%EC%84%9C-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0-1-tesseract
# https://github.com/madmaze/pytesseract
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(r'C:\Users\User\Desktop\ahk\Capture3.png', lang='kor+eng', config='-c preserve_interword_spaces=1 --psm 4'))

