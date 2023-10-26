# Training (GEO01)
# JCY oct 23
# PRO DB PY

import tkinter as tk
# from tkinter.messagebox import showinfo          # Les alertes
import random
from math import sqrt
import time
import database
import datetime
from tkinter.messagebox import *

# Main window
# graphical variables
l = 1000 # canvas length
h = 500 # canvas height
target_x = 10 # x & y to find
target_y = 10
scale = 50 #100 pixels for x=1
mycircle= None #objet utilisé pour le cercle rouge


#important data (to save)
pseudo="Gaston" #provisory pseudo for user
exercise="GEO01"
nbtrials=0 #number of total trials
nbsuccess=0 #number of successfull trials


# on canvas click, check if succeded or failed
def canvas_click(event):
    global mycircle, nbtrials, nbsuccess
    # x et y clicked
    click_x = (event.x - l/2) / scale
    click_y = -(event.y - h/2) / scale

    # distance between clicked and (x,y)
    dx = abs(click_x - target_x)
    dy = abs(click_y - target_y)
    d =  sqrt((dx)**2 + (dy)**2) # Pythagore

    # display a red circle where clicked (global variable mycircle)
    mycircle=circle(target_x,target_y,0.5,"red")

    # check succeeded or failed
    nbtrials+=1
    if d > 0.5:
        window.configure(bg="red")

    else:
        window.configure(bg="green")
        nbsuccess+=1
    lbl_result.configure(text=f"{pseudo} Essais réussis : {nbsuccess} / {nbtrials}")
    window.update()
    time.sleep(1) # delai 1s
    next_point(event=None)


def circle(x,y,r,color):
    #circle, center x & y, r radius, color
    mycircle=canvas.create_oval((x - r) * scale + l/2, -(y-r) * scale + h/2, (x + r) * scale + l/2, -(y + r)* scale + h/2, fill=color)
    return mycircle


def next_point(event):
    global target_x, target_y, mycircle
    window.configure(bg=hex_color)#remettre couleur normale
    print("next_point " + str(event))
    #Clearing the canvas
    canvas.delete('all')

    # x & y axis
    canvas.create_line(0, h/2, l, h/2, fill="black")  # x
    canvas.create_line(l/2, 0, l/2, h, fill="black")  # y

    # x & y random
    target_x = round(random.uniform(-10, 10),0)
    target_y = round(random.uniform(-5, 5),0)

    # display x & y, 1 decimal
    lbl_target.configure(text=f"Cliquez sur le point ({round(target_x, 1)}, {round(target_y, 1)}). Echelle x -10 à +10, y-5 à +5")


window = tk.Tk()
window.title("Exercice de géométrie")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)

# Canvas creation
lbl_title = tk.Label(window, text=f"{exercise}", font=("Arial", 15))
# lbl_title.pack(ipady=5, padx=5,pady=5)
lbl_title.grid(row=0, column=0, padx=5, pady=5, columnspan=6)

tk.Label(window, text='Pseudo:', font=("Arial", 15)).grid(row=1, column=0, padx=5, pady=5)
entry_pseudo = tk.Entry(window, font=("Arial", 15))
# entry_pseudo.pack(ipadx=2, ipady=10, padx=5,pady=5)
entry_pseudo.grid(row=1, column=1)

# lbl_result = tk.Label(window, text=f"{pseudo}  Essais réussis : 0/0", font=("Arial", 15))
lbl_result = tk.Label(window, text=f"Essais réussis : 0/0", font=("Arial", 15))
# lbl_result.pack( ipady=5, padx=5,pady=5)
lbl_result.grid(row=1, column=3, padx=5, pady=5, columnspan=4)

lbl_target = tk.Label(window, text="", font=("Arial", 15))
# lbl_target.pack( ipady=5, padx=5,pady=5)
lbl_target.grid(row=2, column=0, padx=5, pady=5, columnspan=6)

canvas = tk.Canvas(window, width=l, height=h, bg="#f9d893")
# canvas.pack(ipady=5, padx=5,pady=5)
canvas.grid(row=4, column=0, padx=5, pady=5, columnspan=6)
btn_next = tk.Button(window, text="Suivant", font=("Arial", 15))
# btn_next.pack(ipady=5, padx=5,pady=5)
btn_next.grid(row=5, column=0, padx=5, pady=5, columnspan=6)

# first call of next_point
next_point(event=None)

# Association de la fonction au clic sur le canvas
canvas.bind("<Button-1>", canvas_click)
btn_next.bind("<Button-1>", next_point)

start_date = datetime.datetime.now()


# main loop
window.mainloop()
