# Training (INFO05)
# JCY oct 23
# PRO DB PY

import tkinter as tk
from tkinter.messagebox import showinfo          # Les alertes
import random
from math import sqrt
import time

# Main window
# graphical variables
l = 1000 # canvas length
h = 600 # canvas height


#important data (to save)
pseudo="Gaston" #provisory pseudo for user
exercise="INFO05 *************** EN TRAVAUX *******************"
nbtrials=0 #number of total trials
nbsuccess=0 #number of successfull trials

#next color
def next_color():
    print("suivant !")

window = tk.Tk()
window.title("La couileur perdue")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)

# Canvas creation
lbl_title = tk.Label(window, text=f"{exercise}", font=("Arial", 15))
lbl_title.pack(ipady=5, padx=5,pady=5)
lbl_result = tk.Label(window, text=f"{pseudo}  Essais réussis : 0/0", font=("Arial", 15))
lbl_result.pack( ipady=5, padx=5,pady=5)
lbl_target = tk.Label(window, text="", font=("Arial", 15))
lbl_target.pack( ipady=5, padx=5,pady=5)
canvas = tk.Canvas(window, width=l, height=h, bg="#f9d893")
canvas.pack(ipady=5, padx=5,pady=5)
btn_next =tk.Button(window, text="Suivant", font=("Arial", 15))
btn_next.pack(ipady=5, padx=5,pady=5)

# first call of next_point


# Association de la fonction au clic sur le canvas
btn_next.bind("<Button-1>", next_color)

# main loop
window.mainloop()
