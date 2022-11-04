import time, pyautogui,random,string

text = 'laland'
letters = string.ascii_lowercase
window_open = 20

while True:
    time.sleep(4)
    for i in range(window_open):
        time.sleep(random.uniform(0.4,0.6))
        text = "".join(random.choice(letters)for i in range(6))
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl", "t")

    pyautogui.hotkey("ctrl", "tab")
    
    for i in range(window_open):
        pyautogui.hotkey("ctrl", "w")


    input("Presione enter")

