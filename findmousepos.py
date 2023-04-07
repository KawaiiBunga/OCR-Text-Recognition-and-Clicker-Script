import pyautogui

while True:
    x, y = pyautogui.position()
    print(f'Current mouse position: {x}, {y}')
