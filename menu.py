#############################
# Training (Menu)
# JCY oct 23
# PRO DB PY
#############################

import tkinter as tk
import geo01
import info02
import info05
from database import *
from tkinter import *
import tkinter.font

# exercises array
a_exercise=["geo01", "info02", "info05"]
albl_image=[None, None, None] # label (with images) array
a_image=[None, None, None] # images array
a_title=[None, None, None] # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}


# call other windows (exercices)
def exercise(event,exer):
    dict_games[exer](window)


#call display_result
def display_result(event):
    global results_frame, entry_user, entry_ex, up_frame

    window = Tk()

    window.title("Affichage braintraining")
    window.geometry("1100x900")

    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window.configure(bg=hex_color)
    window.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

    lbl_title_results = tk.Label(window, text="TRAINING:AFFICHAGE", font=("Arial", 15))
    lbl_title_results.grid(row=0, column=1, ipady=5, padx=40, pady=40)

    up_frame = Frame(window,bg="white")
    down_frame = Frame(window, bg="white")
    filter_frame = Frame(up_frame,bg="white", padx=10)

    title_total_frame = Frame(down_frame, bg="white", padx=10)
    total_frame = Frame(down_frame, bg="white", padx=10)

    lbl_user = Label(filter_frame, text="Pseudo :", bg="white", padx=40, font=("Arial,11"))
    lbl_ex = Label(filter_frame, text="Exercice :", bg="white", padx=40, font=("Arial,11"))
    lbl_startdate = Label(filter_frame, text="Date début :", bg="white", padx=40, font=("Arial,11"))
    lbl_enddate = Label(filter_frame, text="Date fin :", bg="white", padx=40, font=("Arial,11"))

    title_total = Label(title_total_frame, text="Total", bg="white", padx=40, font=("Arial,11"))

    lbl_tot = Label(total_frame, text="NbLignes", bg="white", padx=40, font=("Arial, 11"))
    lbl_time = Label(total_frame, text="Temps total", bg="white", padx=40, font=("Arial, 11"))
    lbl_nbok = Label(total_frame, text="Nb OK", bg="white", padx=40, font=("Arial, 11"))
    lbl_nbtotal = Label(total_frame, text="Nb Total", bg="white", padx=40, font=("Arial, 11"))
    lbl_purcenttot = Label(total_frame, text="% Total", bg="white", padx=40, font=("Arial, 11"))

    entry_user = Entry(filter_frame)
    entry_ex = Entry(filter_frame)
    entry_startdate = Entry(filter_frame)
    entry_enddate = Entry(filter_frame)

    button_result = Button(filter_frame, text="Voir résultats", font=("Arial,11"), command= show_info)

    up_frame.grid(row=1,column=0,columnspan=3)
    down_frame.grid(row=2,column=0,pady=10,columnspan=3)

    filter_frame.grid(row=1, columnspan=3)

    lbl_user.grid(row=0, column=0, padx=(0, 10))
    entry_user.grid(row=0, column=1)

    lbl_ex.grid(row=0, column=2, padx=(0, 10))
    entry_ex.grid(row=0, column=3)

    lbl_startdate.grid(row=0, column=4, padx=(0, 10))
    entry_startdate.grid(row=0, column=5)

    lbl_enddate.grid(row=0, column=6, padx=(0, 10))
    entry_enddate.grid(row=0, column=7)

    button_result.grid(row=1, column=0, pady=5)

    #TOTAL
    title_total_frame.grid(row=3, pady=10 ,columnspan=3)
    title_total.grid(row=3, pady=10 ,columnspan=3)

    total_frame.grid(row=4, pady=10 ,columnspan=3)

    lbl_tot.grid(row=0, column=0, padx=(0, 10))
    lbl_time.grid(row=0, column=1, padx=(0, 10))
    lbl_nbok.grid(row=0, column=2, padx=(0, 10))
    lbl_nbtotal.grid(row=0, column=3, padx=(0, 10))
    lbl_purcenttot.grid(row=0, column=4, padx=(0, 10))

    window.mainloop()
    print("display_result")


def show_info():
    global results_frame,number

    number = 0

    success_percentage = 0

    open_dbconnection()

    name = infos_results(entry_user.get(), entry_ex.get())
    if number > 0:
        results_frame.destroy()
    results_frame = Frame(up_frame, bg="white", padx=10)
    number += 1

    lbl_col_student = Label(results_frame, text="Élève", bg="white", padx=40, font=("Arial,11"))
    lbl_col_date_hour = Label(results_frame, text="Date heure", bg="white", padx=40, font=("Arial,11"))
    lbl_col_time = Label(results_frame, text="Temps", bg="white", padx=40, font=("Arial,11"))
    lbl_col_ex = Label(results_frame, text="Exercice", bg="white", padx=40, font=("Arial,11"))
    lbl_col_nbok = Label(results_frame, text="nb OK", bg="white", padx=40, font=("Arial,11"))
    lbl_col_nbtot = Label(results_frame, text="nb Total", bg="white", padx=40, font=("Arial,11"))
    lbl_col_reussi = Label(results_frame, text="% réussi", bg="white", padx=40, font=("Arial,11"))

    results_frame.grid(row=2, pady=10 ,columnspan=3)

    lbl_col_student.grid(row=0, column=0, padx=(0, 10))
    lbl_col_date_hour.grid(row=0, column=1, padx=(0, 10))
    lbl_col_time.grid(row=0, column=2, padx=(0, 10))
    lbl_col_ex.grid(row=0, column=3, padx=(0, 10))
    lbl_col_nbok.grid(row=0, column=4, padx=(0, 10))
    lbl_col_nbtot.grid(row=0, column=5, padx=(0, 10))
    lbl_col_reussi.grid(row=0, column=6, padx=(0, 10))
    lbl_col_progress = Label(results_frame, text="Progression", bg="white", padx=40, font=("Arial,11"))
    lbl_col_progress.grid(row=0, column=7, padx=(0, 10))

    i = 0
    for student in name:
        for j in range(len(student)):
            for data in range(len(student[j])):
                if data != 3:
                    values = Label(results_frame, width=10, text=student[j][data])
                else:
                    values = Label(results_frame, width=10, text=get_exercice_name(student[j][data]))
                values.grid(row=j + 1, column=i + data)
            try:
                success_percentage = round(float(student[j][4]) * 100 / float(student[j][5]), 2)
                values = Label(results_frame, width=10, text=f"{success_percentage}%")
            except:
                values = Label(results_frame, width=10, text="0%")
            values.grid(row=j + 1, column=i + 6)

            progress_rect = Canvas(results_frame, width=100, height=20, bg="white", bd=0, highlightthickness=0)
            if success_percentage == 0:
                progress_rect.create_rectangle(0, 0, 1, 20, fill=get_color(success_percentage), outline="")
            else:
                progress_rect.create_rectangle(0, 0, success_percentage, 20, fill=get_color(success_percentage),outline="")
            progress_rect.grid(row=j + 1, column=7, pady=5)
        i = i + 1


def get_color(percentage):
    if percentage >= 70:
        return "#00FF00"  # Green
    elif 40 <= percentage < 70:
        return "#FFA500"  # Orange
    else:
        return "#FF0000"  # Red

# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0,1,2), minsize=300, weight=1)

# Title création
lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

# labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex]=tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1+2*(ex//3),column=ex % 3 , padx=40,pady=10) # 3 label per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
    albl_image[ex] = tk.Label(window, image=a_image[ex]) # put image on label
    albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
    albl_image[ex].bind("<Button-1>", lambda event, ex = ex :exercise(event=None, exer=a_exercise[ex])) #link to others .py
    print(a_exercise[ex])

# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1+ 2*len(a_exercise)//3 , column=1)
btn_display.bind("<Button-1>",lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2+ 2*len(a_exercise)//3 , column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()
