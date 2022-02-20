5분 다찾고 >6분 다찾고 >7분다찾아야하는데 (스크롤마우스휠기능아직안넣음) /n
5분찾고 멈추다가 /n
6분찾고 계속거기에서 멈춤..ㅜ /n

해결! 5분>6분>7분 돌아간돠아!!+_+ return과 break의 위치 /n
근데 왜 이미지를 못찾지? (예시이미지가 스크린안에 있는데 말이야)...ㅜ /n

<킴영감>/n
```
ImageSearch, X, Y, 0, 0, A_ScreenWidth, A_ScreenHeight, *30 image\jm5.bmp
MsgBox, %X%, %Y%
```
01)역슬러시가 맞다/n
02)ahk파일 위치 아래 image폴더안에/n
03)이미지저장시, '24비트 bmp' 또는 'png' /n
04)파일명은 영어이름으로/n

`CoordMode, Mouse, Screen ;마우스동작기준`
05)기본 활성화되어있는 창기준인데 전체로 바꾸고싶다면
```
CoordMode, Pixel, Screen ;전체화면기준
CoordMode, Mouse, Screen
```

나는 왜 아예 `msgbox, %errorlevel%`  메시지박스가안뜨는데?? 뭔일../n

06)듀얼모니터라서?/n
<https://www.youtube.com/watch?v=it-tCqGinZU>
나는 오른쪽이 주모니터 Screen (0,0) (1919,1079) /n
왼쪽모니터는 Screen(-1920, 0) (-1,1079)