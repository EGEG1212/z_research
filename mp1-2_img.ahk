F2:: 
MsgBox, ������մϴ�.
Reload

F4::
MsgBox, �����մϴ�.
ExitApp  


F3::
CoordMode, Pixel ;, Screen
;CoordMode, Mouse, Screen
ImageSearch, X, Y, 0, 0, A_ScreenWidth, A_ScreenHeight, image\jm4.bmp
;MsgBox, %ErrorLevel%
MsgBox, %X%, %Y%

;if (ErrorLevel = 2) {
;	MsgBox ��Ÿ����
;}
;else if (ErrorLevel = 1) {
;	MsgBox Icon could not be found on the screen.
;}
;else if (ErrorLevel = 0) {
;	MsgBox The icon was found at %X%x%Y%.
;}
;else {
;	MsgBox nothing
;}

