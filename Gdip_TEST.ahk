#include Gdip_All.ahk
#include Gdip_ImageSearch.ahk
pToken := Gdip_StartUp()


;pBitmap := Gdip_CreateBitmapFromFile("Capture.png")

;pBitmap := Gdip_BitmapFromScreen("1") ; or "123|456|234|567"
;Gdip_SaveBitmapToFile(pBitmap, A_Desktop "\Result.png")

pBitmap := Gdip_BitmapFromHwnd(WinExist("제목 없음 - 그림판"))
pNeedle := Gdip_CreateBitmapFromFile("Pencil.png")
result := Gdip_ImageSearch(pHaystack, pNeedle, outputVar)



;Gdip_GetImageDimensions(pBitmap, outputWidth, outputHeight)
;MsgBox, % "너비: " outputWidth ", 높이: " outputHeight

;Gdip_DisposeImage(pBitmap)

Gdip_DisposeImage(pHaystack)
Gdip_DisposeImage(pNeedle)
Gdip_Shutdown(pToken)

if (result = 1)
{
    RegExMatch(outputVar, "(.*),(.*)", out)
    MsgBox, X: %out1% Y: %out2%
}

ExitApp
