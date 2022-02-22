F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  

; 220222 +스크롤(마우스휠) +active 로지창활성화
F3::
ST = 500 ; 0.5초
DT = 1000 ; 1초
Loop{
	CoordMode, Pixel, Screen
	part4min:
	Loop{ 
		ImageSearch, FX, FY, 830, 0, 1360, 720, *100 image\jm5.png
		if (errorlevel = 0 ) {
			;MsgBox, 미배5img찾았음갱신하기 %FX%,%FY%
			MouseClick, L, FX+15, FY+15
			SendInput ^g
			Sleep ST
			SendInput {space}
			Sleep DT
			ImageSearch, FX, FY,830, 0, 1360, 720, *100 image\jiyun_NoReaction.PNG
			if (errorlevel = 0) {
				;MsgBox,지연안내img찾았다 %FX%,%FY%
				MouseClick, L, FX+15, FY+15
				sleep ST
				goto part4min
			}
			else if (errorlevel = 1) {
				MsgBox, 지연안내컬럼어딨누test
			}
		}
		else if (errorlevel = 1){
			;MsgBox, errorlevel:%errorlevel%미배차5분없음 6분찾으러넘어가겠음
			goto part5min
		}
	}return
	part5min:
	Loop{
		ImageSearch, FX, FY,830, 0, 1360, 720, *100 image\jm6.bmp
		if (errorlevel = 0 ) {
			MsgBox, 미배차6img찾았음갱신하기 %FX%,%FY%
			MouseClick, L, FX+15, FY+15
			SendInput ^g
			Sleep ST
			SendInput {space}
			Sleep DT
			ImageSearch, FX, FY,830, 0, 1360, 720, *100 image\firstGet_Reaction.PNG
			if (errorlevel = 0 ) {
				;MsgBox, 최접경과img찾았다 %FX%,%FY%
				MouseClick, L, FX+15, FY+15
				sleep ST
				goto part5min
			}			
			else if (errorlevel = 1) {
				MsgBox, 최접결과컬럼어딨누test
			}
		}
		else if (errorlevel = 1) {
			;MsgBox, errorlevel:%errorlevel%미배차6없음 7분찿으러넘어가겠음
			goto part6min
		}
	}
	part6min:
	Loop{
		ImageSearch, FX, FY,830, 0, 1360, 720, *100 image\jm7.png
		if (errorlevel = 0 ) {
			;MsgBox, 미배차7img찾았다갱신하기 %FX%,%FY%
			MouseClick, L, FX+15, FY+15
			SendInput ^g
			Sleep ST
			SendInput {space}
			Sleep DT
			ImageSearch, FX, FY,830, 0, 1360, 720,*100 image\ks.png
			if (errorlevel = 0 ) {
				;MsgBox, 검색img찾았다 %FX%,%FY%
				MouseClick, L, FX+15, FY+15
				sleep ST
				goto part6min
			}			
			else if (errorlevel = 1) {
				MsgBox, 검색버튼어딨누test
			}
		}
		else if (errorlevel = 1) {
			;MsgBox, errorlevel:%errorlevel%미배차7분없음 5분으로 돌아가겠음
			goto part4min
		}
	}
}return


  