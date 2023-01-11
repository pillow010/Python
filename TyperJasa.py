import tkinter
from tkinter import W

import pyautogui

# is an app to help user to input/entry master setting of "JASA"

main_window = tkinter.Tk()
main_window.geometry("600x300")


tkinter.Label(main_window, text="start date:")\
    .grid(row=0, column=0, sticky=W, pady=2)  # Start Year Period
tkinter.Label(main_window, text="*01/01/2022 or 01012022")\
    .grid(row=0, column=2, sticky=W, pady=2)  # year_example
tkinter.Label(main_window, text="end date:")\
    .grid(row=1, column=0, sticky=W, pady=2)  # End Year Period
tkinter.Label(main_window, text="*01/01/2022 or 01012022")\
    .grid(row=1, column=2, sticky=W, pady=2)  # year_example
tkinter.Label(main_window, text="% non penindak langsung")\
    .grid(row=2, column=0, sticky=W, pady=2)  # percentage of penindak langsung
tkinter.Label(main_window, text="% penindak langsung")\
    .grid(row=3, column=0, sticky=W, pady=2)  # percentage of non penindak langsung
# tkinter.Label(main_window, text="% D operator")\
#     .grid(row=4, column=0, sticky=W, pady=2)  # percentage of dokter operator share
# tkinter.Label(main_window, text="% perawat")\
#     .grid(row=5, column=0, sticky=W, pady=2)  # percentage of perawat share
# tkinter.Label(main_window, text="% radiografer")\
#     .grid(row=6, column=0, sticky=W, pady=2)  # percentage of radiografer share


# FIELD TEXT_BOX
startDate = tkinter.Entry(main_window)
endDate = tkinter.Entry(main_window)
nonLangsung = tkinter.Entry(main_window)
langsung = tkinter.Entry(main_window)
PelaksanaSatu = tkinter.Entry(main_window)
PelaksanaDua = tkinter.Entry(main_window)
PelaksanaTiga = tkinter.Entry(main_window)
PelaksanaEmpat = tkinter.Entry(main_window)
Perulangan = tkinter.Entry(main_window)
perulangan_value = tkinter.IntVar()
tkinter.Checkbutton(main_window, text="Jumlah Perulangan",
                    variable=perulangan_value).grid(row=8, column=0, sticky=W, pady=2)

# TEXT_BOX POSITIONING
startDate.grid(row=0, column=1)
endDate.grid(row=1, column=1)
nonLangsung.grid(row=2, column=1)
langsung.grid(row=3, column=1)
PelaksanaSatu.grid(row=4, column=1)
PelaksanaDua.grid(row=5, column=1)
PelaksanaTiga.grid(row=6, column=1)
PelaksanaEmpat.grid(row=7, column=1)
Perulangan.grid(row=8, column=1)


def tunai():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')  # <==alt tab

    pyautogui.press('f5')  # Setting Group
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(startDate.get()))
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
    pyautogui.write(str(endDate.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('kelo')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(nonLangsung.get()))
    pyautogui.hotkey('alt', 't')
    pyautogui.write('kelom')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(langsung.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('up')
    pyautogui.press('f5')
    pyautogui.write('non')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('f5')
    pyautogui.write(str(clickedPelaksanaSatu.get()))
    pyautogui.press('tab')
    pyautogui.write(str(PelaksanaSatu.get()))
    if clickedPelaksanaDua.get() != "Pilih Satu":
        pyautogui.hotkey('alt', 't')
        pyautogui.write(str(clickedPelaksanaDua.get()))
        pyautogui.press('tab')
        pyautogui.write(str(PelaksanaDua.get()))
    if clickedPelaksanaTiga.get() != "Pilih Satu":
        pyautogui.hotkey('alt', 't')
        pyautogui.write(str(clickedPelaksanaTiga.get()))
        pyautogui.press('tab')
        pyautogui.write(str(PelaksanaTiga.get()))
    if clickedPelaksanaEmpat.get() != "Pilih Satu":
        pyautogui.hotkey('alt', 't')
        pyautogui.write(str(clickedPelaksanaEmpat.get()))
        pyautogui.press('tab')
        pyautogui.write(str(PelaksanaEmpat.get()))

    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked


def jaminan():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')  # <==alt tab

    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(startDate.get()))
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
    pyautogui.write(str(endDate.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('in')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write('12')
    pyautogui.hotkey('alt', 't')
    pyautogui.write('ke')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write('88')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('f5')
    pyautogui.write('kelo')
    pyautogui.press('tab')
    pyautogui.write(str(nonLangsung.get()))
    pyautogui.hotkey('alt', 't')
    pyautogui.write('kelom')
    pyautogui.press('tab')
    pyautogui.write(str(langsung.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('up')
    pyautogui.press('f5')
    pyautogui.write('non')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('f5')
    pyautogui.write(str(clickedPelaksanaSatu.get()))
    pyautogui.press('tab')
    pyautogui.write(str(PelaksanaSatu.get()))
    if clickedPelaksanaDua.get() != "Pilih Satu":
        pyautogui.hotkey('alt', 't')
        pyautogui.write(str(clickedPelaksanaDua.get()))
        pyautogui.press('tab')
        pyautogui.write(str(PelaksanaDua.get()))
    if clickedPelaksanaTiga.get() != "Pilih Satu":
        pyautogui.hotkey('alt', 't')
        pyautogui.write(str(clickedPelaksanaTiga.get()))
        pyautogui.press('tab')
        pyautogui.write(str(PelaksanaTiga.get()))
    if clickedPelaksanaEmpat.get() != "Pilih Satu":
        pyautogui.hotkey('alt', 't')
        pyautogui.write(str(clickedPelaksanaEmpat.get()))
        pyautogui.press('tab')
        pyautogui.write(str(PelaksanaEmpat.get()))

    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked


def repeating():
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.hotkey('shiftleft', 'shiftright', 'tab')
    pyautogui.hotkey('shiftleft', 'shiftright', 'tab')


# Dropdown menu options
options = [
    "Pilih Satu",
    "Apoteker",
    "Analis Lab",
    "Bidan",
    "Dokter Anastesi",
    "Dokter Operator",
    "Dokter Umum",
    "Fisioterapis",
    "Perawat",
    "Radiografer"
]


# datatype of menu text
clickedPelaksanaSatu = tkinter.StringVar(main_window)
clickedPelaksanaDua = tkinter.StringVar(main_window)
clickedPelaksanaTiga = tkinter.StringVar(main_window)
clickedPelaksanaEmpat = tkinter.StringVar(main_window)


# initial menu text
clickedPelaksanaSatu.set(options[0])
clickedPelaksanaDua.set(options[0])
clickedPelaksanaTiga.set(options[0])
clickedPelaksanaEmpat.set(options[0])


# Create Dropdown menu
dropPelaksanaSatu = tkinter.OptionMenu(main_window, clickedPelaksanaSatu, *options)
dropPelaksanaSatu.grid(row=4, column=0, sticky=W, pady=2)

dropPelaksanaDua = tkinter.OptionMenu(main_window, clickedPelaksanaDua, *options)
dropPelaksanaDua.grid(row=5, column=0, sticky=W, pady=2)

dropPelaksanaTiga = tkinter.OptionMenu(main_window, clickedPelaksanaTiga, *options)
dropPelaksanaTiga.grid(row=6, column=0, sticky=W, pady=2)

dropPelaksanaEmpat = tkinter.OptionMenu(main_window, clickedPelaksanaEmpat, *options)
dropPelaksanaEmpat.grid(row=7, column=0, sticky=W, pady=2)


def printselectedcheckbox():
    # print("satu ", (clickedPelaksanaSatu.get() == "Pilih Satu"))
    # print("dua ", (clickedPelaksanaDua.get() == "Pilih Satu"))
    # print("tiga ", (clickedPelaksanaTiga.get() == "Pilih Satu"))
    # print("empat ", (clickedPelaksanaEmpat.get() == "Pilih Satu"))
    if clickedPelaksanaSatu.get() != "Pilih Satu":
        print("satu ", clickedPelaksanaSatu.get())
    else:
        if clickedPelaksanaDua.get() != "Pilih Satu":
            print("dua ", clickedPelaksanaDua.get())
        else:
            if clickedPelaksanaTiga.get() != "Pilih Satu":
                print("tiga ", clickedPelaksanaTiga.get())
            else:
                if clickedPelaksanaEmpat.get() != "Pilih Satu":
                    print("empat ", clickedPelaksanaEmpat.get())

    if clickedPelaksanaSatu.get() != "Pilih Satu":
        print("satu ", clickedPelaksanaSatu.get())
    if clickedPelaksanaDua.get() != "Pilih Satu":
        print("dua ", clickedPelaksanaDua.get())
    if clickedPelaksanaTiga.get() != "Pilih Satu":
        print("tiga ", clickedPelaksanaTiga.get())
    if clickedPelaksanaEmpat.get() != "Pilih Satu":
        print("empat ", clickedPelaksanaEmpat.get())
    # print("satu "+clickedPelaksanaSatu.get() + " Pilih Satu " + clickedPelaksanaSatu.get() == "Pilih Satu")
    # print("dua "+clickedPelaksanaDua.get() + " Pilih Satu " + clickedPelaksanaDua.get() == "Pilih Satu")
    # print("tiga "+clickedPelaksanaTiga.get() + " Pilih Satu " + clickedPelaksanaTiga.get() == "Pilih Satu")
    # print("empat "+clickedPelaksanaEmpat.get() + " Pilih Satu " + clickedPelaksanaEmpat.get() == "Pilih Satu")
    # print("satu "+PelaksanaSatu.get())
    # print("dua "+PelaksanaDua.get())
    # print("tiga "+PelaksanaTiga.get())
    # print("empat "+PelaksanaEmpat.get())


printButton = tkinter.Button(main_window, text="click Me", command=printselectedcheckbox)
printButton.grid(row=9, column=0, sticky=W, pady=2)


tombolJaminan = tkinter.Button(main_window, text="JAMINAN", command=jaminan)
tombolJaminan.grid(row=9, column=1)


tombolTunai = tkinter.Button(main_window, text="TUNAI", command=tunai)
tombolTunai.grid(row=9, column=2)

if __name__ == "__main__":
    main_window.mainloop()
