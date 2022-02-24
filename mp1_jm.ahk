F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  

; 클릭^g갱신후, (먼클릭안하고) image\jm4.png jm5.png jm6.bmp
;...검색영역조절 (검색영역 줄여서 계속검색: 검색이미지가 워낙작다보니, px조절) -> 클릭위치y를 5로 줄이고, 검색영역 10밑으로 수정
;...너무 스크롤&wheelDown계속해서 문제ㅠ(날짜내림차순정렬하니 그럴필요없다) -> wheelDown삭제
;...마우스대기위치(계속한자리에있으니 마우스오버되어 이미지가려짐) -> mousemove 1100,40
;ㅁ로그인 및 ahk실행 F3
;ㅁ하단콜리스트 없애기
;ㅁ탁송제외 체크
;ㅁ날짜정렬(내림차순)

F3::
Loop{
	ST := 500 ; 0.5초
	DT := 1000 ; 1초
	CoordMode, Pixel, Screen
	cnt := 0
	SY := 126
	MouseMove 1100, 40
	part4min:
	Loop{
		ImageSearch, FX, FY, 923, SY, 1360, 720, *100 image\jm4.png
		if (errorlevel = 0 ) {
			MouseClick, L, FX+15, FY+5
			MouseGetPos, X, Y
			SendInput ^g
			Sleep ST
			SendInput {space}
			Sleep DT
			;검색영역조절SY
			SY := Y+10
			goto part4min
		}
		else if (errorlevel = 1){
			ImageSearch, FX, FY, 1330, 116, 1365, 147, *100 image\scr.bmp
			if (errorlevel = 0 and cnt<4) {
				ImageSearch, FX, FY, 1334, 130, 1365, 673, *100 image\srcb.bmp
				MouseClickDrag, left, FX+15, FY+15, FX+15, 160, 1
				;send, {WheelDown 7}
				cnt += 1
				goto part4min
			}
			else {
				break
			}
		}
	}
	cnt := 0
	SY := 126
	MouseMove 1100, 40
	part5min:
	Loop{
		ImageSearch, FX, FY, 923, SY, 1360, 720, *100 image\jm5.png
		if (errorlevel = 0 ) {
			MouseClick, L, FX+15, FY+5
			SendInput ^g
			Sleep ST
			SendInput {space}
			Sleep DT
			;검색영역조절SY
			SY := FY+10
			goto part5min
		}
		else if (errorlevel = 1){
			ImageSearch, FX, FY, 1330, 116, 1365, 147, *100 image\scr.bmp
			if (errorlevel = 0 and cnt<4) {
				ImageSearch, FX, FY, 1334, 130, 1365, 673, *100 image\srcb.bmp
				MouseClickDrag, left, FX+15, FY+15, FX+15, 160, 1
				;send, {WheelDown 7}
				cnt += 1
				goto part4min
			}
			else {
				break
			}
		}
	}
	cnt := 0
	SY := 126
	MouseMove 1100, 40
	part6min:
	Loop{
		ImageSearch, FX, FY, 923, SY, 1360, 720, *100 image\jm6.bmp
		if (errorlevel = 0 ) {
			MouseClick, L, FX+15, FY+5
			SendInput ^g
			Sleep ST
			SendInput {space}
			Sleep DT
			;검색영역조절SY
			SY := FY+10
			goto part6min
		}
		else if (errorlevel = 1){
			ImageSearch, FX, FY, 1330, 116, 1365, 147, *100 image\scr.bmp
			if (errorlevel = 0 and cnt<4) {
				ImageSearch, FX, FY, 1334, 130, 1365, 673, *100 image\srcb.bmp
				MouseClickDrag, left, FX+15, FY+15, FX+15, 160, 1
				;send, {WheelDown 7}
				cnt += 1
				goto part4min
			}
			else {
				;break
				goto part4min
			}
		}
	}
}
