from asyncio import Handle
import pyautogui


#five_btn = pyautogui.locateOnScreen('jm4.PNG')
#five_btn = pyautogui.locateOnScreen('jm5.PNG')
#five_btn = pyautogui.locateOnScreen('jm6.bmp')
#five_btn = pyautogui.locateOnScreen('tszz.png') #탁송제외
#five_btn = pyautogui.locateOnScreen('img_clist.png') #콜리스트
# print(five_btn)
# pyautogui.moveTo(five_btn)
# pyautogui.moveRel(0, -3)
# pyautogui.dragTo(0, 300, 2, button='left')
#pyautogui.dragRel(0, 500, button='left')
#pyautogui.click(34, 27)

#열려있는모든창정보
# for win in pyautogui.getAllWindows():
#    print(win)

from pywinauto.application import Application
app = Application.Application()
app.start('../SmartD2/daeri.exe')