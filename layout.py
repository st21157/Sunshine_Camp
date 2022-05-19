# Created: 20/05/2022 | 20 May 2022
# Author: Kheona Taracatac

"""
- all the visual stuff
"""

from tkinter import *

root = Tk()

# labels + entries
Label(root, text="Leader").grid(row=1, column=1)
ent_leader = Entry(root).grid(row=1, column=2)

Label(root, text="# of Campers").grid(row=3, column=1)

Label(root, text="Location").grid(row=1, column=3)
ent_location = Entry(root).grid(row=1, column=4)

Label(root, text="Weather").grid(row=3, column=3)
ent_weather = Entry(root).grid(row=3, column=4)



root.mainloop() # exclude when importing
