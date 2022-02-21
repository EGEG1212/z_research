F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  


F3::
ST = 500 ; 0.5초
DT = 1000 ; 1초
;영역안에서(스크린 또는 윈도우 ahk_class SmartD2-)  / Loop범위수정?? / 못찾는거면 윈도우돋보기 / 이미지파일명에 *100 *30해보기
;loop{5찾고 클릭 ^g 검색버튼} 0의 경우 return
;							1의경우 다음으로 흘러가게둔다
;loop{6찾고 클릭 ^g 검색버튼}
;loop{7찾고 클릭 ^g 검색버튼}
;없다면 스크롤다운
;없다면 스크롤업

Loop{
	;WinActivate ahk_exe DAERI.EXE
	Loop{ 
		CoordMode Pixel
		ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jm4.bmp ;본컴 C:/Users/Administrator/Desktop/mp1-ggg/jm5.png ;노트북 
		if (errorlevel = 0 ) {
			MsgBox, 미배차4img찾았다 %FX%,%FY%
			;MouseMove, FX+15, FY+10 ;혹쉬콤마때문인가했쥐....
			;MouseClick, L, FX+15, FY+10
			;send ^g
			sleep ST
			;send {space}
			;sleep DT
			;큰검색버튼 클릭
			ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jiyun_NoReaction.PNG
			if (errorlevel = 0) {
				MsgBox,지연안내img찾았다 %FX%,%FY%
				;MouseMove FX+15, FY+10
				;MouseClick, L, FX+15, FY+15
				sleep ST
				;break  ;다음loop로 가버림.. (더 찾으란 말이다ㅏㅏㅏ)
				;return ;여기서 잠수타버림. 어디로 갔냐ㅑㅑㅑㅑㅑㅑㅑㅑㅑ
			}
			else if (errorlevel = 1) {
				MsgBox, 지연안내컬럼어딨누 
				sleep DT
				send {Esc}
			}
		}
		else if (errorlevel = 1){
			MsgBox, 미배차4분없음
			SendInput {Esc}
			break ;다음 5분으로 안넘어가고 그냥 끝나버림???? 5분으로 넣어가야해ㅜㅜㅜㅜㅜ
		}
	}return
	Loop{
		ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jm5.bmp
		if (errorlevel = 0 ) {
			MsgBox, 미배차5img찾았다 %FX%,%FY%
			;MouseMove FX+15, FY+10
			;MouseClick, L, FX+15, FY+10
			;send ^g
			sleep ST
			;send {space}
			;sleep DT
			;큰검색버튼 클릭
			ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\firstGet_Reaction.PNG
			if (errorlevel = 0 ) {
				MsgBox, 최접경과img찾았다 %FX%,%FY%
				;MouseMove FX+15, FY+10
				;MouseClick, L, FX+15, FY+15
				;sleep ST
				return
			}			
			else if (errorlevel = 1) {
				MsgBox, 최접결과컬럼어딨누
				sleep DT
				SendInput {Esc}
			}
		}
		else if (errorlevel = 1) {
			MsgBox, 미배차5분없음
			SendInput {Esc}
			break
		}
	}
	Loop{
		ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jm6.bmp
		if (errorlevel = 0 ) {
			MsgBox, 미배차6img찾았다 %FX%,%FY%
			;MouseMove FX+15, FY+10
			;MouseClick, L, FX+15, FY+10
			;send ^g
			sleep ST
			;send {space}
			;sleep DT
			;큰검색버튼 클릭
			ImageSearch, FX, FY, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\ks.png
			if (errorlevel = 0 ) {
				MsgBox, 검색img찾았다 %FX%,%FY%
				;MouseMove FX+15, FY+10
				;MouseClick, L, FX+15, FY+15
				;sleep ST
				return
			}			
			else if (errorlevel = 1) {
				MsgBox, 검색버튼어딨누
				sleep DT
				SendInput {Esc}
			}
		}
		else if (errorlevel = 1) {
			MsgBox, 미배차6분없음
			SendInput {Esc}
			break
			
		}
	}
}return


  