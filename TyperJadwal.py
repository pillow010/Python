import tkinter
from tkinter import ttk
import datetime
from tkinter import W
import pyautogui
import time


main_window = tkinter.Tk()
main_window.geometry("1000x200")

# Dropdown menu options
listDokter = [
    "Pilih Dokter",
    "Alma Thahir Pulungan",
    "Amalia K. Mansur",
    "Andrian Wulur",
    "Beriman Parhusip",
    "Canang Irving Amrizal",
    "Chandra Irawan",
    "Chrisming Wiraja",
    "Dadang Herdiana",
    "Darma Putra Sitepu",
    "Deny Handayanto",
    "Desak",
    "Desy Nur Arista",
    "Diah Kusuma Wardani",
    "Dini Zuriana",
    "Eka Pranata",
    "Elisabeth Handayani",
    "Endi Permana Utomo",
    "Firman Sah Anthonius",
    "Heldrian Dwi Nanda",
    'Hendriko Sitorus',
    "Ieke Harsya Barliana",
    "Ika Fransisca",
    "Irfan Mulyana Mustofa",
    "Kandita Arjani",
    "Made Wira bhawa",
    "Margi Yati Soewito",
    "Miko Galastri",
    "Muhamad Mulyadi",
    "Muhammad Relly",
    "Muslimah Luhuna",
    "Ni Nyoman Tri Priliawati",
    "Ni'ma Nuraini Kusuma Sari",
    "Norman Rabker Jefret Tuhulele",
    "Nurul Subhan",
    "Pipik Ripai",
    "R. Leni Maelani Patimah",
    "RANGGA KUSUMA MAULANA",
    "Renie Astriani F",
    "Rina Rahmayani",
    "Rini Suryani",
    "Satria Evo B",
    "Setya Budi Hutapea",
    "Tegoeh Winandar",
    "Tengku Budiansyah",
    "Titty Sulianty",
    "Wahyu Sigit Purnomo",
    "Widja Widajaka",
    "Widya Sakti Pratama",
    "Yati Nurhayati",
    "Yulia Santi Eko Wulansari",
    "Yuliantry Indah Lestari",
    "Zam Zam Firmansyah"

]

# datatype of menu text
clickedDokter = tkinter.StringVar(main_window)

# initial menu text
clickedDokter.set(listDokter[0])

# Create Dropdown menu
dropDokter = ttk.Combobox(main_window, textvariable=clickedDokter, values=listDokter)

# LABEL
tkinter.Label(main_window, text="Sec B4 Start:")\
    .grid(row=0, column=0, sticky=W, pady=2)  # sleep_label
tkinter.Label(main_window, text="Year:")\
    .grid(row=1, column=0, sticky=W, pady=2)  # year_label
tkinter.Label(main_window, text="Month")\
    .grid(row=2, column=0, sticky=W, pady=2)  # month_label
# tkinter.Label(main_window, text="Doctor")\
#     .grid(row=3, column=0, sticky=W, pady=2)  # doctor_label
dropDokter.grid(row=3, column=0, sticky=W, pady=2)
tkinter.Label(main_window, text="Holiday")\
    .grid(row=4, column=0, sticky=W, pady=2)  # holiday_label
# tkinter.Label(main_window, text="Days")\
#     .grid(row=2, column=2, sticky=W, pady=2)  # days_label
tkinter.Label(main_window, text="|Quota Reservasi|")\
    .grid(row=0, column=3, sticky=W, pady=2)  # rsv_doctor_quota_label
tkinter.Label(main_window, text="|Quota Langsung|")\
    .grid(row=0, column=4, sticky=W, pady=2)  # spot_doctor_quota_label


# label3 = tkinter.Label(main_window, text="Senin").grid(row=2)

# FIELD TEXT_BOX
hold_field = tkinter     .Entry(main_window)
year_field = tkinter     .Entry(main_window)
month_field = tkinter    .Entry(main_window)
# doctor_field = tkinter   .Entry(main_window)
holiday_field = tkinter  .Entry(main_window)  # Holiday
rsv_doctor_quota = tkinter.Entry(main_window, width=4)
spot_doctor_quota = tkinter.Entry(main_window, width=4)
rsv_doctor_quota1 = tkinter.Entry(main_window, width=4)
spot_doctor_quota1 = tkinter.Entry(main_window, width=4)


# TEXT_BOX POSITIONING
hold_field     .grid(row=0, column=1)
year_field     .grid(row=1, column=1)
month_field    .grid(row=2, column=1)
# doctor_field   .grid(row=3, column=1)
holiday_field  .grid(row=4, column=1)   # Holiday
rsv_doctor_quota.grid(row=1, column=3)
spot_doctor_quota.grid(row=1, column=4)
rsv_doctor_quota1.grid(row=3, column=3)
spot_doctor_quota1.grid(row=3, column=4)

# FALUE CHECKBOX 1 CHECKED 0 UNCHECK
monday_value = tkinter   .IntVar()
tuesday_value = tkinter  .IntVar()
wednesday_value = tkinter.IntVar()
thursday_value = tkinter .IntVar()
friday_value = tkinter   .IntVar()
saturday_value = tkinter .IntVar()
monday_value1 = tkinter   .IntVar()
tuesday_value1 = tkinter  .IntVar()
wednesday_value1 = tkinter.IntVar()
thursday_value1 = tkinter .IntVar()
friday_value1 = tkinter   .IntVar()
saturday_value1 = tkinter .IntVar()

monday_checkbox = tkinter\
    .Checkbutton(main_window, text="Monday",
                 variable=monday_value)
tuesday_checkbox = tkinter\
    .Checkbutton(main_window, text="Tuesday",
                 variable=tuesday_value)
wednesday_checkbox = tkinter\
    .Checkbutton(main_window, text="Wednesday",
                 variable=wednesday_value)
thursday_checkbox = tkinter\
    .Checkbutton(main_window, text="Thursday",
                 variable=thursday_value)
friday_checkbox = tkinter\
    .Checkbutton(main_window, text="Friday",
                 variable=friday_value)
saturday_checkbox = tkinter\
    .Checkbutton(main_window, text="Saturday",
                 variable=saturday_value)
monday_checkbox1 = tkinter\
    .Checkbutton(main_window, text="Monday",
                 variable=monday_value1)
tuesday_checkbox1 = tkinter\
    .Checkbutton(main_window, text="Tuesday",
                 variable=tuesday_value1)
wednesday_checkbox1 = tkinter\
    .Checkbutton(main_window, text="Wednesday",
                 variable=wednesday_value1)
thursday_checkbox1 = tkinter\
    .Checkbutton(main_window, text="Thursday",
                 variable=thursday_value1)
friday_checkbox1 = tkinter\
    .Checkbutton(main_window, text="Friday",
                 variable=friday_value1)
saturday_checkbox1 = tkinter\
    .Checkbutton(main_window, text="Saturday",
                 variable=saturday_value1)

# CHECKBOX POSITIONING FOR THE DAYS
monday_checkbox     .grid(row=1, column=5, sticky=W, pady=2)
tuesday_checkbox    .grid(row=1, column=6, sticky=W, pady=2)
wednesday_checkbox  .grid(row=1, column=7, sticky=W, pady=2)
thursday_checkbox   .grid(row=1, column=8, sticky=W, pady=2)
friday_checkbox     .grid(row=1, column=9, sticky=W, pady=2)
saturday_checkbox   .grid(row=1, column=10, sticky=W, pady=2)
monday_checkbox1     .grid(row=3, column=5, sticky=W, pady=2)
tuesday_checkbox1    .grid(row=3, column=6, sticky=W, pady=2)
wednesday_checkbox1  .grid(row=3, column=7, sticky=W, pady=2)
thursday_checkbox1   .grid(row=3, column=8, sticky=W, pady=2)
friday_checkbox1     .grid(row=3, column=9, sticky=W, pady=2)
saturday_checkbox1   .grid(row=3, column=10, sticky=W, pady=2)


def before_date():
    pyautogui.press('f5')
    # pyautogui.write(re.sub(r"[\n\t]", "", str(doctor_field.get())))
    pyautogui.write(dropDokter.get())
    pyautogui.press('tab')
    return []


def type_after_date():
    pyautogui.press('tab')
    pyautogui.write('7')
    pyautogui.press('tab')
    pyautogui.write('14')
    pyautogui.press('tab')
    pyautogui.write(rsv_doctor_quota.get())
    pyautogui.press('tab')
    pyautogui.write(spot_doctor_quota.get())
    return []


def before_date1():
    pyautogui.press('f5')
    # pyautogui.write(re.sub(r"[\n\t]", "", str(doctor_field.get())))
    pyautogui.write(dropDokter.get())
    pyautogui.write()
    pyautogui.press('tab')
    return []


def type_after_date1():
    pyautogui.press('tab')
    pyautogui.write('7')
    pyautogui.press('tab')
    pyautogui.write('14')
    pyautogui.press('tab')
    pyautogui.write(rsv_doctor_quota1.get())
    pyautogui.press('tab')
    pyautogui.write(spot_doctor_quota1.get())
    return []


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)


def last_day_of_selected_month():
    cek_tanggal_terakhir = (last_day_of_month(datetime.date(int(year_field.get()), int(month_field.get()), 1)))
    return cek_tanggal_terakhir.strftime("%d")


def monday():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '0':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date())
    return []


def tuesday():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '1':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date())
    return []


def wednesday():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '2':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date())
    return []


def thursday():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '3':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date())
    return []


def friday():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '4':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date())
    return []


def saturday():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '5':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date())
    return []


def monday1():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '0':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date1())
    return []


def tuesday1():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '1':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date1())
    return []


def wednesday1():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '2':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date1())
    return []


def thursday1():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '3':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date1())
    return []


def friday1():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '4':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date1())
    return []


def saturday1():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        if str(datetime.date(int(year_field.get()), int(month_field.get()), day).weekday()) == '5':
            pyautogui.run(before_date())
            pyautogui.write(str(f"{day:02d}"))
            pyautogui.run(type_after_date1())
    return []


def run_command():
    time.sleep(int(hold_field.get()))
    if monday_value     .get() == 1:
        pyautogui       .run(monday())
    if tuesday_value    .get() == 1:
        pyautogui       .run(tuesday())
    if wednesday_value  .get() == 1:
        pyautogui       .run(wednesday())
    if thursday_value   .get() == 1:
        pyautogui       .run(thursday())
    if friday_value     .get() == 1:
        pyautogui       .run(friday())
    if saturday_value   .get() == 1:
        pyautogui       .run(saturday())
    if rsv_doctor_quota1.get() != 0:
        if monday_value1.get() == 1:
            pyautogui.run(monday1())
        if tuesday_value1.get() == 1:
            pyautogui.run(tuesday1())
        if wednesday_value1.get() == 1:
            pyautogui.run(wednesday1())
        if thursday_value1.get() == 1:
            pyautogui.run(thursday1())
        if friday_value1.get() == 1:
            pyautogui.run(friday1())
        if saturday_value1.get() == 1:
            pyautogui.run(saturday1())
    pyautogui.press('f9')


def next_level():
    for day in range(1, int(last_day_of_selected_month())+1):
        if str(f"{day:02d}") in str(holiday_field.get()).split(',') or str(day) in str(holiday_field.get()).split(','):
            continue
        pyautogui.run(before_date())
        pyautogui.write(str(f"{day:02d}"))
    pyautogui.press('f9')


# tombol = tkinter.Button(main_window, text="Next Level", command=run_command)
# tombol.grid(row=6, column=4)
# tombol.bind('<Return>', run_command)

tombol = tkinter.Button(main_window, text="GO TYPE", command=run_command)
tombol.grid(row=6, column=0)
tombol.bind('<Return>', run_command)


if __name__ == "__main__":
    main_window.mainloop()
