# Training (INFO02)
# JCY oct 23
# PRO DB PY

import tkinter as tk
import random
from math import pow
import time

#important data (to save)
pseudo="Gaston" #provisory pseudo for user
exercise="INFO02"
nbtrials=0 #number of total trials
nbsuccess=0 #number of successfull trials

# Liaison entre le canvas et le code
unite = ["B", "kB", "MB", "GB", "TB"]
n1 = 0  # valeur à convertir
u1 = unite[0]
n2 = 0  # valeur à convertir
u2 = unite[0]
rapport = 0

def next(event):
    global n1, u1, u2, rapport
    window.configure(bg=hex_color)

    n1 = round(random.random(), 3)
    dec = random.randint(0, 3)
    for i in range(dec):
        n1 *= 10
    n1 = round(n1, 3)
    p1 = random.randint(1, 4)
    u1 = unite[p1]
    p2 = p1
    while p1 == p2:
        p2 = random.randint(0, 4)
    u2 = unite[p2]
    rapport = pow(10, 3 * (p2 - p1))
    label_n1.configure(text=f" {n1} {u1} =")
    label_u2.configure(text=f" {u2} ")
    entry_n2.delete(0,'end')

def test(event):
    global n2, nbsuccess, nbtrials
    # Fonction pour tester si la valeur est juste
    n2 = float(entry_n2.get())
    nbtrials+=1
    success = (abs(n1 / n2 / rapport - 1) < 0.01)
    if success:
        nbsuccess += 1
        window.configure(bg="green")
    else:
        window.configure(bg="red")
    lbl_result.configure(text=f"{pseudo} Essais réussis : {nbsuccess} / {nbtrials}")
    window.update()
    time.sleep(1) # delai 1s
    next(event=None)

window = tk.Tk()
window.title("Conversion d'unités")
window.geometry("1100x900")
window.grid_columnconfigure((0,1,2), minsize=150, weight=1)

# color definition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)

lbl_title = tk.Label(window, text=f"{exercise}", font=("Arial", 15))
lbl_title.grid(row=0,column=0,columnspan=3, ipady=5, padx=20,pady=20)
lbl_result = tk.Label(window, text=f"{pseudo}  Essais réussis : 0/0", font=("Arial", 15))
lbl_result.grid( row=1, column=0,columnspan=3, ipady=5, padx=20,pady=20)

label_n1 = tk.Label(window, text="n1:",font=("Arial", 15))
label_n1.grid(row=2,column=0,ipady=5, padx=20,pady=20,sticky='E')

entry_n2 = tk.Entry(window,font=("Arial", 15))
entry_n2.grid(row=2,column=1,ipady=5,padx=5, pady=20,sticky='E')
entry_n2.bind("<Return>", test)

label_u2 =tk.Label(window, text="u2:",font=("Arial", 15))
label_u2.grid(row=2,column=2,ipady=5,padx=5,pady=20,sticky='W')

btn_next =tk.Button(window, text="Suivant", font=("Arial", 15))
btn_next.grid(row=3,column=0,columnspan=3,ipady=5, padx=5,pady=5)
btn_next.bind("<Button-1>", next)

# first call of next_point
next(event=None)

# Main loop
window.mainloop()
