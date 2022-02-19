### download
AutoHotKey
(https://www.autohotkey.com/download/)

### Editor
SciTE4AutoHotkey
(https://fincs.ahk4.net/scite4ahk/)

### F2키를 눌렀을때 alert MsgBox popUp
```
F2::
MsgBox, Hello World!!
```

### 
`Send, Hello!`
키보드입력 Hello

### 마우스위치 찾아주는 spy를 참조.
`Click, 100 200`
윈도우기준

### 활성화된 윈도우영역 (0,0),(200,150) 안에서 이미지 찾기
```
F3::
ImageSearch, X, Y, 251, 470, 835, 705, *100 test.png
MouseMove, %X%, %Y%
#또는
Click, %X%, %Y%
```

### 캡쳐: 윈도우+shift+s
근데 저장위치는 어디?ㅋㅋ
🎈캡쳐를 1/4정도로 떠야한다.
이미지의 왼쪽위를 클릭하기 때문에..

### 윈도우말고 스크린영역으로 바꾸겠다.
CoordMode, Pixel, Screen
CoordMode, Mouse, Screen
```
F3::
CoordMode, Pixel, Screen
CoordMode, Mouse, Screen
ImageSearch, X, Y, 75, 0, 1813, 800, *100 test.png
MouseMove,  %X%, %Y%
```

### errorlevel 결과확인
```
F3::
ImageSearch, X, Y, 251, 470, 835, 705, *100 test.png
MsgBox, %ell
```
0 : 이미지 찾음
1 : 이미지 못 찾음
2 : 기타 에러 발생

### macro 종료
```
return

F4::
ExitApp
```
ExitApp 윗 단에`return` 해줘야 흐르지 않음.

### 이미지 찾으면 좌표출력, 못 찾으면 지정된 문구 출력
```
F3::
CoordMode, Pixel, Screen
CoordMode, Mouse, Screen
ImageSearch, X, Y, 75, 0, 1813, 800, *100 test.png
if (errorlevel=0) {
    MsgBox, %X%, %Y%
}
else if (errorlevel=1) {
    MsgBox, failed to find image
}
return

F4::
ExitApp
```

### 반복문
```
Loop {

}
```

### insta 좋아요 > 다음버튼
```
F3::
Loop{
	Loop {
		ImageSearch, X, Y, 629, 518, 1067, 897, *100 test.png
		if (errorlevel = 0) {
			Click, %X%, %Y%
			Break
		}
		else if (errorlevel=1) {
			Sleep, 1000
		}	
	}
	ImageSearch, X, Y, 629, 518, 1067, 897, *100 next.png
	Click, %X%, %Y%
	Sleep, 1000
}
return

F4::
ExitApp
```