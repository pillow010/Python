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


def TypeRegPasien():                # SET PT -> EXCEL -> BO
    # pyautogui.hotkey('alt', 'tab')  # EXCEL
    # pyautogui.press('tab')
    # pyautogui.keyDown('alt')
    # pyautogui.keyUp('alt')          # BO
    pyautogui.hotkey('alt','t')
    pyautogui.hotkey('alt','n')
    pyautogui.press('tab')
    # tab // pasien
    # lama
    # tab
    # tab // pasien
    # baru
    # spasi
    # nama ->
    # tab
    # tempat
    # lahir
    # tab
    # tab
    # tanggal
    # lahir
    # tab
    # 4
    # x
    # kelamin
    # arow
    # kiri
    # male
    # kanan
    # female
    # tab
    # 14
    # x
    # alamat
    # tab
    # rt
    # tab
    # rw
    # tab
    # telfon
    # tab
    # telfon
    # tab
    # kodepos
    # tab
    # enter
    # kodya
    # dll
    # alt
    # y
    # enter
    # alt
    # y
    # tanggal -> manual
    # alt
    # o
    # enter
    # alt
    # s


tombol = tkinter.Button(main_window, text="GO TYPE", command=TypeRegPasien)
tombol.grid(row=6, column=4)
# main_window.bind('<space>', lambda event: TypeBO())

if __name__ == "__main__":
    main_window.mainloop()
