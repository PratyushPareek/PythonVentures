import pyperclip
import pyautogui
import time

#pyautogui.hotkey('alt','tab')

pyautogui.tripleClick(536,296)
# pyautogui.keyDown('shift')
# pyautogui.keyDown('down')
# pyautogui.pause = 8
# pyautogui.keyUp('shift')
# pyautogui.keyUp('down')
pyautogui.hotkey('ctrl','c')
para = pyperclip.paste()
pyautogui.click(1653,59)
pyautogui.click(532,579)

pyautogui.typewrite(para)