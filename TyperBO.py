import pyautogui
import tkinter
import os
from tkinter import W

main_window = tkinter.Tk()
main_window.geometry("1000x200")
# main_window.attributes("-topmost", True)

numberingEntry = tkinter.Entry(main_window)
numberingEntry.grid(row=0, column=1)
tkinter.Label(main_window, text="Number Start From:")\
    .grid(row=0, column=0, sticky=W, pady=2)

pyautogui.PAUSE = 0.1


def TypeBO():       # SET PT -> EXCEL -> BO
    pyautogui.hotkey('alt', 'tab')  # EXCEL
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')          # BO
    for i in range(5):
        pyautogui.hotkey('alt', 's')
        pyautogui.press('space')
        pyautogui.hotkey('alt', 'tab')  # EXCEL
        pyautogui.press('return')
        pyautogui.press('f2')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')  # BO
        pyautogui.hotkey('alt', 't')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('shiftleft', 'shiftright', 'tab')
        pyautogui.write(str(f"{int(numberingEntry.get()) + i:03d}"))

# def forceStop():
#     os.system("taskkill /f /im python.exe")
#
# def TypeTest():
#     pyautogui.hotkey('alt', 'tab')
#     pyautogui.write(str(f"{int(numberingEntry.get()) + 1:03d}"))


# tombol = tkinter.Button(main_window, text="TEST TYPE", command=TypeTest)
# tombol.grid(row=6, column=3)
# main_window.bind('F3', lambda event: TypeBO())

tombol = tkinter.Button(main_window, text="GO TYPE", command=TypeBO)
tombol.grid(row=6, column=4)
main_window.bind('<space>', lambda event: TypeBO())

# kill = tkinter.Button(main_window, text="KILL", command=forceStop)
# kill.grid(row=6, column=5)
# main_window.bind('<F4>', lambda event: forceStop())

if __name__ == "__main__":
    main_window.mainloop()
