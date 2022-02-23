F2:: 
MsgBox, 재시작합니다.
Reload

F4::
MsgBox, 종료합니다.
ExitApp  


gugudan(dan)
{
    a := 0
    Loop, 9
        result .= dan " x " A_Index " = " dan * A_Index "`n"
    MsgBox, %result%
    return
}

F3::
gugudan(7)
gugudan(8)
gugudan(9)
return

