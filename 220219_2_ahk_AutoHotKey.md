### download
AutoHotKey
<https://www.autohotkey.com/download/>

### Editor
SciTE4AutoHotkey
<https://fincs.ahk4.net/scite4ahk/>
*Window spy 필수*
...혹쉬.. notepad++을 쓴다면? 다운&설정참고 <https://www.youtube.com/watch?v=i-moTBJZ1nA>

#### Help 참고
<https://www.autohotkey.com/docs/commands/MouseClick.htm>

### 🤩OCR문자인식 
<https://ahkplant.tistory.com/354>

### 코드변경시, 계속 재접속😫...
```
F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  
```
😋머릿글에 꼭 넣자!!!
아예 첫문장을 입력해버린다!?<https://secretgd.tistory.com/212?category=713787>
C: -> Window -> ShellNew -> Template.ahk 안에 입력하면<br>
바탕화면에 마우스우클릭-> 새로만들기 -> AutoHotkey Script 🤩짜잔

### Symbol의 의미
| Symbol| 의미 |
|:--:|:--:|
| ^| Ctrl |
| !| Alt |
| +| Shift |
|'#| Windows |
|{특수키}| Tap, Enter, PgUp, PgDn 등|

핫키를 잠시 막고싶을땐, Suspend

## Run
Hotkey(단축키) win+n키를 눌렀을때 프로그램 실행. <br>
환경변수설정이 되어있거나(notepad), 경로를 입력하지않으면.. <br>
환경변수설정을 해야한다. 시스템환경 변수 편집->path에 경로추가<https://www.youtube.com/watch?v=RaFHyu1plis&list=PL--lMTarQb9mUzNzxJ-fErRSdQUCXCmkf&index=13>25:25
```
#n::
	Run Notepad
    ;Run, www.naver.com, Max ;Max|Min|Hide 택1
	;Run, www.naver.com, ,Max
	;Run, chrome.exe "www.naver.com" ;🙃띄어쓰기 꼭
	Run, C:\Program Files (x86)\ipTIME\ipTIME NAS\Utility\ipTIME_ipDISK_Drive.exe
return
```
줄바꿈안해도 아래와 같다
```
#n:: Run Notepad
```

### Hotkey(단축키) F2키를 눌렀을때 alert MsgBox popUp
```
F2::
MsgBox, Hello World!!
```

### Hotkey(단축키)F2키를 눌렀을때, 키보드입력 Hello
```
F2::
Send, Hello!
return
```


### 마우스위치 찾아주는 spy를 참조.
`Click, 100 200`
윈도우기준 100,200 위치에서 클릭.

### 활성화된 윈도우영역 (0,0),(200,150) 안에서 이미지 찾기
```
F3::
ImageSearch, X, Y, 251, 470, 835, 705, *100 test.png
MouseMove, %X%, %Y%
#또는
Click, %X%, %Y%
```

### 캡쳐: win + shift + s
근데 저장위치는 어디?ㅋㅋ <br>
🎈캡쳐를 1/4정도로 떠야한다. <br>
이미지의 왼쪽위를 클릭하기 때문에.. <br>

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
0 : 이미지 찾음  <br>
1 : 이미지 못 찾음 <br>
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

### 반복문 loop, while, for... 또는 Goto
<https://ahkplant.tistory.com/146> <br>
프날<https://pnal.kr/68>
```
Loop { 
    ;무한반복
} 
return

Loop,3 { 
    ;3회반복
}
return
```

### 조건문 elif는 없다...
```
if (ErrorLevel = 2)
			MsgBox Could not conduct the search.
		else if (ErrorLevel = 1)
			MsgBox Icon could not be found on the screen.
		else
			MsgBox The icon was found at %FoundX%x%FoundY%.
```


### 영역내에서만 단축키활성화 '#IfWinActive'
class명은 spy에서 확인
```
#IfWinActive ahk_class Notepad
	PgUp::A
	#h::MsgBox good
```    
PgUp키를 누르면 A가찍히고  <br>
win+h키를 누르면 alert창에 good 팝업  <br>
이것들은 notepad내에서만 작동함.

## HotStrings(자동고침)
```
::btw::by the way ;끝나다함과 동시에 변경
:*:ily::I Love You ;즉시변경
:?:al::airplane ;앞에어떤글자 있던지 상관없이 al 보이기만하면 치환
:B0:<html>::</html>{left8} ; 근데 left8칸으로 커서가 안옮겨옴??
```
### HotStrings의 input기능
```
::]d::
	formattime, currentdatetime, ,yyyy/M/d h:mm tt
	sendinput %currentdatetime%
return
```
현재 시간 출력   <br>
2022/2/19 7:19 오후

## Remapping Keys
```
#IfWinActive ahk_class Notepad
q::b ;q키를 눌렀을 때, b가 입력됨
LWin::return ; 왼win키를 눌렀을 때, 아무일도 일어나지않음. (먹통)
```
전체 상태에서 리맵핑해버리면 불편한점이 은근 있으니..  <br>
`#IfWinActive`와 함께 쓰는게 좋겠다🙄

### 🎅미니플젝🎅윈도우 안에서의 insta 좋아요 클릭 -> 다음버튼 클릭
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

### 🎅미니플젝🎅엑셀에서 내게쓰기 메일보내기 4번반복
```
#y:: Reload

#,::
ST = 500 ; 0.5초
DT = 2000 ; 2초
loop,4
{
	WinActivate ahk_class XLMAIN ; 엑셀포커스
	sleep ST
	send ^c 					 ; Ctrl + C
	sleep ST
	WinActivate ahk_exe chrome.exe ; 크롬포커스
	sleep ST
	MouseClick L, 465,291 		; 제목칸에 마우스 좌클릭
	sleep ST
	Send ^v 					; Ctrl + V
	sleep ST
	WinActivate ahk_class XLMAIN ; 엑셀포커스
	sleep ST
	send {right}				; 오른쪽 화살표
	sleep ST
	send {F2}					; 엑셀에서 테스트만 복사하려고
	sleep ST
	send ^a
	send ^c 					 ; Ctrl + C
	sleep ST
	send {esc}
	sleep ST
	WinActivate ahk_exe chrome.exe ; 크롬포커스
	sleep ST
	MouseClick L, 329,480 		; 본문칸에 마우스 좌클릭
	Send ^v 					; Ctrl + V
	sleep ST
	ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, C:/Users/User/Desktop/ahk/save.png ; 저장버튼 클릭
	sleep ST
	MouseClick, L, FX+15, FY+15
	Sleep DT
	ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, C:/Users/User/Desktop/ahk/me.png ; 내게쓰기 클릭
	sleep ST
	MouseClick, L, FX+15, FY+15
	Sleep DT
	WinActivate ahk_class XLMAIN ; 엑셀포커스
	sleep ST
	send {left}
	sleep ST
	send {down}
}

return

F4::
ExitApp
```