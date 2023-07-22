import tkinter as tk
from tkinter import W

import pyperclip
import pyautogui
import keyboard
import threading


def updateStatus():
    pyautogui.hotkey('alt', 'u')
    pyautogui.press('down')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('return')


def batalBayar():
    # print('ok')
    pyautogui.hotkey('ctrl', 'c')   # copy tanggal
    tanggal_bayar_field\
        .insert(0, pyperclip.paste())  # simpan tanggal bayar 1
    pyautogui.keyDown('shift')
    for i in range(16):
        pyautogui.press('tab')
    pyautogui.keyUp('shift')
    pyautogui.press('return')  # 23
    pyautogui.write('batal')
    pyautogui.press('tab')
    pyautogui.write('123456')
    pyautogui.hotkey('alt', 'y')
    pyautogui.press('l')
    pyautogui.press('tab')
    pyautogui.write('revisi tarif')
    pyautogui.hotkey('alt', 's')
    for i in range(2):
        pyautogui.press('return')
    pyautogui.hotkey('alt', 'k')
    pyautogui.press('return')


def bayar():
    pyautogui.hotkey('alt', 'y')    # klik bayar
    for i in range(2):
        pyautogui.press('y')
    pyautogui.hotkey('alt', 'y')    # valid klik bayar
    for i in range(7):
        pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'c')   # copy no bayar
    nomor_bayar_field.insert(0, pyperclip.paste())


def updateTanggal():
    pyautogui.hotkey('alt', 'c')
    pyautogui.hotkey('alt', '5')
    pyautogui.write(nomor_bayar_field.get())   # copy tanggal
    pyautogui.hotkey('alt', 'r')
    pyautogui.press('return')
    pyautogui.hotkey('alt', 'u')    # 34
    for i in range(7):
        pyautogui.press('tab')
    pyautogui.write(tanggal_bayar_field.get())
    pyautogui.hotkey('alt', 's')
    pyautogui.write('revisi tarif')
    pyautogui.hotkey('alt', 'y')


def start_updateStatus():
    threading.Thread(target=updateStatus).start()


def start_batalBayar():
    threading.Thread(target=batalBayar).start()


def start_Bayar():
    threading.Thread(target=bayar).start()


def start_updateTanggal():
    threading.Thread(target=updateTanggal).start()


main_window = tk.Tk()
main_window.geometry("1000x200")
main_window.wm_attributes("-topmost", 1)  # Set the window to be always on top

tanggal_bayar_label = tk.Label(main_window, text="Tanggal Bayar")
tanggal_bayar_label.grid(row=0, column=0, sticky=W, pady=2)
tanggal_bayar_field = tk.Entry(main_window)
tanggal_bayar_field.grid(row=0, column=1)
nomor_bayar_label = tk.Label(main_window, text="Nomor Bayar")
nomor_bayar_label.grid(row=1, column=0, sticky=W, pady=2)
nomor_bayar_field = tk.Entry(main_window)
nomor_bayar_field.grid(row=1, column=1)


def copyTanggalBayar():
    pyperclip.copy(tanggal_bayar_field.get())


def copyNomorBayar():
    pyperclip.copy(nomor_bayar_field.get())


tombolCopy1 = tk.Button(main_window, text="copy", command=copyTanggalBayar)
tombolCopy1.grid(row=0, column=2)

tombolCopy2 = tk.Button(main_window, text="copy", command=copyNomorBayar)
tombolCopy2.grid(row=1, column=2)

updateStatusBtn = tk.Button(main_window, text="Update (F2)", command=start_Bayar)
updateStatusBtn.grid(row=3, column=0)

batalBayarBtn = tk.Button(main_window, text="Batal (F3)", command=start_Bayar)
batalBayarBtn.grid(row=3, column=1)

BayarBtn = tk.Button(main_window, text="Bayar (F4)", command=start_updateTanggal)
BayarBtn.grid(row=3, column=2)

updateTanggalBtn = tk.Button(main_window, text="Update Tanggal (F5)", command=start_batalBayar)
updateTanggalBtn.grid(row=3, column=3)

# Bind the F1 key globally using keyboard library
keyboard.add_hotkey('F2', start_updateStatus())
keyboard.add_hotkey('F3', start_batalBayar)
keyboard.add_hotkey('F4', start_Bayar)
keyboard.add_hotkey('F5', start_updateTanggal)


if __name__ == "__main__":
    main_window.mainloop()
