F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  

F3::
Loop{
	Loop{
		MsgBox, loop1
		break
	}
	;return없어도 계속 loop1반복

	Loop{
		MsgBox, loop2
		;Continue ;계속loop2반복인걸???
		break		
	}
	;; return ; 위break과 return이 만나니 그냥 꺼져버림?
	Loop{
		MsgBox, loop3
		goto, My6
	}
	return
	Loop{
		MsgBox, loop4
	}
	return
	My6: 
	MsgBox, My6
	Loop{
		MsgBox, loop6
	}
	return
	
}
return