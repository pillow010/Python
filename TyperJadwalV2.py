import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import W
import pyautogui
import time

main_window = tk.Tk()
main_window.geometry("1000x200")

# Dropdown menu options
listDokter = [
    "Pilih Dokter",
    "Alma Thahir Pulunga",
    # "Amalia K. Mansur",
    # "Andrian Wulur",
    # "Beriman Parhusip",
    "Canang Irving A",
    "Chandra Irawan",
    "Chrisming Wiraja",
    "Dadang Herdiana",
    "Darma Putra Sitepu",
    # "Deny Handayanto",
    "Desak Gede Arie Y",
    "Desy Nur Arista",
    "Diah Kusuma Wardani",
    "Dini Zuriana",
    "Eka Pranata",
    "Elisabeth Handayani",
    # "Endi Permana Utomo",
    "Firman Sah A",
    "Heldrian DS",
    'Hendriko',
    "Ieke H. Barliana",
    "Ika Fransisca",
    "Irfan Mulyana M",
    "Kandita Arjani",
    "M. Mulyadi",
    "Made Wirabhawa",
    "Margi Yati S",
    "Miko Galastri",
    "Muhammad Relly",
    "Muslimah Luhuna",
    "Ni Nyoman Tri P",
    "Ni'ma Nuraini Kusuma Sari",
    # "Norman Rabker Jefret Tuhulele",
    "Nurul Subhan",
    "Pipik Ripai",
    "R. Leni Maelani P",
    "RANGGA KUSUMA M",
    "Renie Astriani F",
    "Rina Rahmayani",
    "Rini Suryanti",
    "Satria Evo B",
    "Setia Budi Hutapea",
    "Tegoeh Winandar",
    "Tengku Mohammad B",
    "Titty Sulianty",
    # "Wahyu Sigit Purnomo",
    "Widja Widajaka",
    "Widya Sakti Pratama",
    "Yati Nurhayati",
    "Yulia S E W",
    # "Yuliantry Indah L",
    "Zam Zam Firmansyah"

]

# datatype of menu text
clickedDokter = tk.StringVar(main_window)

# initial menu text
clickedDokter.set(listDokter[0])

# Create Dropdown menu
dropDokter = ttk.Combobox(main_window, textvariable=clickedDokter, values=listDokter)

# LABEL
tk.Label(main_window, text="Sec B4 Start:") \
    .grid(row=0, column=0, sticky=W, pady=2)  # sleep_label
tk.Label(main_window, text="Year:") \
    .grid(row=1, column=0, sticky=W, pady=2)  # year_label
tk.Label(main_window, text="Month") \
    .grid(row=2, column=0, sticky=W, pady=2)  # month_label
dropDokter.grid(row=3, column=0, sticky=W, pady=2)
tk.Label(main_window, text="Holiday") \
    .grid(row=4, column=0, sticky=W, pady=2)  # holiday_label
tk.Label(main_window, text="|Quota Reservasi|") \
    .grid(row=0, column=3, sticky=W, pady=2)  # rsv_doctor_quota_label
tk.Label(main_window, text="|Quota Langsung|") \
    .grid(row=0, column=4, sticky=W, pady=2)  # spot_doctor_quota_label

# FIELD TEXT_BOX
hold_field = tk.Entry(main_window)
year_field = tk.Entry(main_window)
month_field = tk.Entry(main_window)
holiday_field = tk.Entry(main_window)  # Holiday
rsv_doctor_quota = tk.Entry(main_window, width=4)
spot_doctor_quota = tk.Entry(main_window, width=4)
rsv_doctor_quota1 = tk.Entry(main_window, width=4)
spot_doctor_quota1 = tk.Entry(main_window, width=4)

# Get the current date
current_date = datetime.date.today()

# Calculate the next month and year
next_month1 = current_date.month + 1
next_year = current_date.year

# Adjust if the next month exceeds 12
if next_month1 > 12:
    next_month1 = 1
    next_year += 1

# Pre Value
hold_field.insert(0, str('2'))
year_field.insert(0, str(next_year))
month_field.insert(0, str(next_month1))

# TEXT_BOX POSITIONING
hold_field.grid(row=0, column=1)
year_field.grid(row=1, column=1)
month_field.grid(row=2, column=1)
holiday_field.grid(row=4, column=1)  # Holiday
rsv_doctor_quota.grid(row=1, column=3)
spot_doctor_quota.grid(row=1, column=4)
rsv_doctor_quota1.grid(row=3, column=3)
spot_doctor_quota1.grid(row=3, column=4)

# FALUE CHECKBOX 1 CHECKED 0 UNCHECK
monday_value = tk.IntVar()
tuesday_value = tk.IntVar()
wednesday_value = tk.IntVar()
thursday_value = tk.IntVar()
friday_value = tk.IntVar()
saturday_value = tk.IntVar()
monday_value1 = tk.IntVar()
tuesday_value1 = tk.IntVar()
wednesday_value1 = tk.IntVar()
thursday_value1 = tk.IntVar()
friday_value1 = tk.IntVar()
saturday_value1 = tk.IntVar()

monday_checkbox = tk\
    .Checkbutton(main_window, text="Monday",
                 variable=monday_value)
tuesday_checkbox = tk \
    .Checkbutton(main_window, text="Tuesday",
                 variable=tuesday_value)
wednesday_checkbox = tk \
    .Checkbutton(main_window, text="Wednesday",
                 variable=wednesday_value)
thursday_checkbox = tk \
    .Checkbutton(main_window, text="Thursday",
                 variable=thursday_value)
friday_checkbox = tk \
    .Checkbutton(main_window, text="Friday",
                 variable=friday_value)
saturday_checkbox = tk \
    .Checkbutton(main_window, text="Saturday",
                 variable=saturday_value)
monday_checkbox1 = tk \
    .Checkbutton(main_window, text="Monday",
                 variable=monday_value1)
tuesday_checkbox1 = tk \
    .Checkbutton(main_window, text="Tuesday",
                 variable=tuesday_value1)
wednesday_checkbox1 = tk \
    .Checkbutton(main_window, text="Wednesday",
                 variable=wednesday_value1)
thursday_checkbox1 = tk \
    .Checkbutton(main_window, text="Thursday",
                 variable=thursday_value1)
friday_checkbox1 = tk \
    .Checkbutton(main_window, text="Friday",
                 variable=friday_value1)
saturday_checkbox1 = tk \
    .Checkbutton(main_window, text="Saturday",
                 variable=saturday_value1)

# CHECKBOX POSITIONING FOR THE DAYS
monday_checkbox.grid(row=1, column=5, sticky=W, pady=2)
tuesday_checkbox.grid(row=1, column=6, sticky=W, pady=2)
wednesday_checkbox.grid(row=1, column=7, sticky=W, pady=2)
thursday_checkbox.grid(row=1, column=8, sticky=W, pady=2)
friday_checkbox.grid(row=1, column=9, sticky=W, pady=2)
saturday_checkbox.grid(row=1, column=10, sticky=W, pady=2)
monday_checkbox1.grid(row=3, column=5, sticky=W, pady=2)
tuesday_checkbox1.grid(row=3, column=6, sticky=W, pady=2)
wednesday_checkbox1.grid(row=3, column=7, sticky=W, pady=2)
thursday_checkbox1.grid(row=3, column=8, sticky=W, pady=2)
friday_checkbox1.grid(row=3, column=9, sticky=W, pady=2)
saturday_checkbox1.grid(row=3, column=10, sticky=W, pady=2)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def process_weekday(weekday):
    """
    Process appointments for a selected weekday in the month.

    Args:
        weekday (int): The integer representation of the weekday (0 for Monday, 1 for Tuesday, and so on).
    """
    for day in range(1, int(last_day_of_selected_month()) + 1):
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == str(weekday):
            pyautogui.press('f5')
            pyautogui.write(dropDokter.get())
            pyautogui.press('tab')
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.press('tab')
            pyautogui.write('7')
            pyautogui.press('tab')
            pyautogui.write('14')
            pyautogui.press('tab')
            if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get())\
                    .split(','):
                pyautogui.write('0')
                pyautogui.press('tab')
                pyautogui.write('0')
            else:
                pyautogui.write(rsv_doctor_quota.get())
                pyautogui.press('tab')
                pyautogui.write(spot_doctor_quota.get())


def last_day_of_month(any_day):
    """Calculate the last day of the month for a given date."""
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def last_day_of_selected_month():
    """Get the last day of the selected month."""
    cek_tanggal_terakhir = last_day_of_month(datetime.date(int(year_field.get()), int(month_field.get()), 1))
    return cek_tanggal_terakhir.strftime("%d")


def run_command():
    """Run the appointment processing based on selected weekdays."""
    time.sleep(int(hold_field.get()))
    weekdays_to_process = [0, 1, 2, 3, 4, 5]  # Monday to Saturday
    for weekday in weekdays_to_process:
        if globals()[f"{weekdays[weekday].lower()}_value"].get() == 1:   # get checkbox status
            process_weekday(weekday)                                     # run weekday
        if globals()[f"{weekdays[weekday].lower()}_value1"].get() == 1:  # get checkbox status
            process_weekday(weekday)                                     # run weekday
    pyautogui.press('f9')


tombol = tk.Button(main_window, text="GO TYPE", command=run_command)
tombol.grid(row=6, column=0)


if __name__ == "__main__":
    main_window.mainloop()
