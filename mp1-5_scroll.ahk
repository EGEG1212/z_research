F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  


/*
    https://expertbuilder.tistory.com/28
*/

F3::
ST = 500 ; 0.5초
DT = 1000 ; 1초
; 220222 +스크롤(마우스휠)send {PgDn} +active 로지창활성화
CoordMode, Pixel, Screen
CoordMode, Mouse, Screen
part4min:
Loop{ 
	ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jm5.bmp
	if (errorlevel = 0 ) {
		MsgBox, 미배5img찾았음갱신하기 %FX%,%FY%
		/*
		MouseClick, L, FX+15, FY+15
		SendInput ^g
		Sleep ST
		SendInput {space}
		Sleep DT
		*/
		ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jiyun_NoReaction.PNG
		if (errorlevel = 0) {
			MsgBox,지연안내img찾았다 %FX%,%FY%
			/*
			MouseClick, L, FX+15, FY+15
			sleep ST
			*/
			goto part4min
		}
		else if (errorlevel = 1) {
			MsgBox, 지연안내컬럼어딨누test
		}
	}
	else if (errorlevel = 1){
		MsgBox, errorlevel:%errorlevel%미배차5분없음 스크롤내려보겠음
		MouseClick, WheelUp, , , 2 
		;goto part5min
	}
}return