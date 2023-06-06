import tkinter
from tkinter import W

import pyautogui
import re

main_window = tkinter.Tk()
main_window.geometry("350x600")

input_frame_row3 = tkinter.Frame(main_window)
input_frame_row3.pack(anchor='w')

sleep_label = tkinter.Label(input_frame_row3, text="sleep")
sleep_label.pack(side='left')

sleep_field = tkinter.Entry(input_frame_row3)
sleep_field.insert(0, "0.4")  # Set default value as 0.4
sleep_field.pack(side='left')

def update_sleep_duration():
    pyautogui.PAUSE = float(sleep_field.get())

update_sleep_duration()

apply_button = tkinter.Button(input_frame_row3, text="Apply", command=update_sleep_duration)
apply_button.pack(side='left')

# pyautogui.PAUSE = 0.1

# Create input fields
input_frame_row1 = tkinter.Frame(main_window)
input_frame_row1.pack(anchor='w')

tanggal_awal_label = tkinter.Label(input_frame_row1, text="tanggal awal ")
tanggal_awal_label.pack(side='left', anchor='w')
tanggal_awal_field = tkinter.Entry(input_frame_row1)
tanggal_awal_field.insert(0, "01/06/2023")  # Set default value
tanggal_awal_field.pack(side='left', anchor='w')

input_frame_row1b = tkinter.Frame(main_window)
input_frame_row1b.pack(anchor='w')

tanggal_akhir_label = tkinter.Label(input_frame_row1b, text="tanggal akhir")
tanggal_akhir_label.pack(side='left')
tanggal_akhir_field = tkinter.Entry(input_frame_row1b)
tanggal_akhir_field.insert(0, "31/12/2030")  # Set default value
tanggal_akhir_field.pack(side='left')

# Create input fields
input_frame_row2 = tkinter.Frame(main_window)
input_frame_row2.pack(anchor='w')

js_label = tkinter.Label(input_frame_row2, text="js")
js_label.pack(side='left')
js_field = tkinter.Entry(input_frame_row2)
js_field.pack(side='left')

jp_label = tkinter.Label(input_frame_row2, text="jp")
jp_label.pack(side='left')
jp_field = tkinter.Entry(input_frame_row2)
jp_field.pack(side='left')


# Checkbox values
checkbox_values = {
    "iccu": 1,
    "opr": 2,
    "tran": 3,
    "vvip": 4,
    "utama": 5,
    "vip": 6,
    "i": 7,
    "ii": 8,
    "hcu": 9,
    "iii": 10,
    "icu": 11,
    "inter": 12,
    "iso": 13,
    "nicu": 14,
    "picu": 15
}


# Create checkbox variables
checkbox_vars = {}
for checkbox_text in checkbox_values.keys():
    checkbox_vars[checkbox_text] = tkinter.IntVar()

# Create checkboxes
for checkbox_text, checkbox_var in checkbox_vars.items():
    checkbox = tkinter.Checkbutton(main_window, text=checkbox_text, variable=checkbox_var, onvalue=1, offvalue=0)
    checkbox.pack(anchor='w')

# def add():
#     for i in range (15):
#         pyautogui.press("f5")
#         # kelas
#         for x in range(i):
#             pyautogui.press("down")
#         pyautogui.press("tab")
#         # tanggal awal
#         pyautogui.write("0162023")
#         pyautogui.press("tab")
#         # tanggal akhir
#         pyautogui.hotkey("ctrl","shiftleft","right")
#         pyautogui.write	("31122030")
#         pyautogui.press("tab")
#         # js
#         pyautogui.write(js_field.get())
#         pyautogui.press("tab")
#         pyautogui.press("tab")
#         pyautogui.write(jp_field.get())


def filter_special_characters(text):
    # Filter out special characters using regular expression
    filtered_text = re.sub(r"[^\w\s]", "", text)
    return filtered_text


# Function to handle the button click event
def add():
    pyautogui.hotkey("alt","tab")
    selected_checkboxes = [checkbox_values[checkbox] for checkbox in checkbox_values.keys() if checkbox_vars[checkbox].get() == 1]


    for checkbox_value in selected_checkboxes:
        print(checkbox_value)
        pyautogui.press("f5")

        # kelas
        for _ in range(checkbox_value):
            pyautogui.press("down")
        pyautogui.press("tab")

        # tanggal awal
        tanggal_awal = filter_special_characters(tanggal_awal_field.get())
        pyautogui.write(tanggal_awal)
        pyautogui.press("tab")

        # tanggal akhir
        tanggal_akhir = filter_special_characters(tanggal_akhir_field.get())
        pyautogui.hotkey("ctrl", "shiftleft", "right")
        pyautogui.write(tanggal_akhir)
        pyautogui.press("tab")

        # js
        pyautogui.write(js_field.get())
        pyautogui.press("tab")
        pyautogui.press("tab")

        # jp
        pyautogui.write(jp_field.get())


tombol = tkinter.Button(main_window, text="START(Enter)", command=add)
tombol.pack()
main_window.bind('<Return>', lambda event: add())

# Function to open a new window with the text
def open_manual_window():
    manual_text = '''
    1. ketika klik "START" atau tekan "SPACE" 
        script akan berjalan
    2. sudah termasuk fungsi alt + tab sehingga 
        posisikan window berjejer
    3. pastikan tanggal awal
    4. check pada kelas yang ingin disetting
    '''
    # Create the manual window
    manual_window = tkinter.Toplevel()
    manual_window.title("Manual")

    # Create a text widget to display the manual text
    manual_text_widget = tkinter.Text(manual_window, height=10, width=50)
    manual_text_widget.insert(tkinter.END, manual_text)
    manual_text_widget.pack()

# # Create the main tkinter window
# window = tkinter.Tk()

# Create the "Manual" button
manual_button = tkinter.Button(main_window, text="Manual(F1)", command=open_manual_window)
manual_button.pack()
main_window.bind('<F1>', lambda event: open_manual_window())


if __name__ == '__main__':
    main_window.mainloop()

