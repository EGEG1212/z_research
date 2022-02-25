### ImageSearch
5분 다찾고 -> 6분 다찾고 -> 7분다찾아야하는데 (스크롤마우스휠기능아직안넣음) <br>
5분찾고 멈추다가 <br>
6분찾고 계속거기에서 멈춤..😨 <br>

해결! 5분->6분->7분 돌아간돠아😀!! return과 break의 위치 <br>
근데 왜 이미지를 못찾지? (예시이미지가 스크린안에 있는데 말이야)...😨 <br>

```
ImageSearch, X, Y, 0, 0, A_ScreenWidth, A_ScreenHeight, *30 image\jm5.bmp
MsgBox, %X%, %Y%
```
01)역슬러시가 맞다<br>
02)ahk파일 위치 아래 image폴더안에<br>
03)이미지저장시, '24비트 bmp' 또는 'png' <br>
04)파일명은 영어이름으로<br>

`CoordMode, Mouse, Screen ;마우스동작기준`  <br>
05)기본 활성화되어있는 창기준인데 전체로 바꾸고싶다면
```
CoordMode, Pixel, Screen ;전체화면기준🧡
CoordMode, Mouse, Screen
```

나는 왜 아예 `msgbox, %errorlevel%`  메시지박스가 안뜨는거지?? 이게뭔일😨<br>
🧡`F2::` 아래에 `msgbox` 넣고
```F4::
ExitApp
 ```
 이건 맨아래두니까 그냥 Exit?!?!? 🧡맨위로 올리기<br>

06)듀얼모니터라서?<br>
<https://www.youtube.com/watch?v=it-tCqGinZU> <br>
나는 오른쪽이 주모니터 Screen (0,0) (1919,1079) <br>
왼쪽모니터는 Screen(-1920, 0) (-1,1079) <br>
 <br>
😀😀😀
```
#y:: Reload
F4::
ExitApp
 
F2::
CoordMode, Pixel ;, Screen
ImageSearch, X, Y, 0, 0, 1920, 1079, *100 image\jm4.bmp
;ImageSearch, X, Y, 0, 0, A_ScreenWidth, A_ScreenHeight, *100 image\jm4.bmp
;MsgBox, %ErrorLevel%
MsgBox, %X%, %Y%
```
.bmp .png 모두 가능! 😀<br>
같은 이미지인데도 왜 두번째 것만 가리키는걸까? `*50, *100, 삭제해도` <br>
🤦‍♀️`*225`는 영 딴곳을 찍음.<br>
ahk너..img차별하는고니?!?😨<br>

<https://blog.naver.com/gmrdud2gh/221556342729> <br>
07)이미지가 작을수록 정확도가 높다. (왠지왠지 크게하면 좋을것같지만, 아님) <br>
08)폴더명 한칸 띄고 파일명? <br>
09)'*정확도50기준?? <br>

#### Devlog.220223 
😥스크롤이 생길정도로 양이 많아지니 엄청 버벅거리더라...<br>
💡검색영역을 조절해서 줄줄이 단위로 검색하도록<br>
💡컬러로 FCFCFC FBFBFB EFEFEF로 스크롤인식 -> 3컬러 or안먹히길래 이미지인식으로ㅋ <br>

#### Devlog.220224
클릭^g갱신후, (먼클릭안하고) image\jm4.png jm5.png jm6.bmp <br>
매크로걸릴까 걱정했는데 게임이 아니니깤ㅋㅋ괜춘 <br>
🧪검색영역조절 (검색영역 줄여서 계속검색: 검색이미지가 워낙작다보니, px조절) -> 클릭위치y를 5로 줄이고, 검색영역 10밑으로 수정 <br>
🧪너무 스크롤&wheelDown계속해서 문제ㅠ(💡날짜내림차순정렬하니 그럴필요없다) -> wheelDown삭제 <br>
💡마우스대기위치(계속한자리에있으니 마우스오버되어 이미지가려짐) -> mousemove 1100,40 <br>
😥환경이 바뀌면 좌표확인해야한다...  <br>
ㅁ로그인 및 ahk실행 F3 <br> 
ㅁ접수상태, 창max <br>
ㅁ하단콜리스트 없애기 <br>
ㅁ탁송제외 체크 <br>
ㅁ날짜정렬(내림차순) <br>
<br>
🧪MouseGetPos 맞게 잘적용했는지? TEST <br>
🧪어제컬러 안되거 혹쉬... or 2개까지되네. 3개는왜안되는거ㅜㅜ? || 또는 | 것도 안됨🤬 <br>
💡이미지일치여부도 확인가능한가? 날짜삼각형^이미지가 맞다면 스크롤만올리고, 틀리다면 클릭 <br>

#### Devlog.220225
😥스크롤이 이미 올라가있는데도 계속 끌어올리느라 바쁨. <br>
😥이미 날짜 내림차순일경우엔 검색영역아래로 조절안해도됨.(클릭갱신즉시 사라지기때문에) <br>
😥검색영역 아래아래 내려가다가 갑자기 뜬금점프? 왜? <br>
🧪TEST<접수,배차 상태로 날짜내림차순> <br>
계속스크롤문제 <br>
(날짜내림차순 괜춘. 배차받은건 날짜로 바뀌기때문에) <br>
중간중간 날짜내림차순정렬안해주면.. 오더섞여있어서 잘못클릭함. space만 먹히면 개별창뜸ㅜ <br>
