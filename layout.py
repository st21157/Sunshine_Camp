# Created: 20/05/2022 | 20 May 2022
# Author: Kheona Taracatac

"""
- all the visual stuff
"""

from tkinter import *

root = Tk()

# labels + entries
Label(root, text="Leader").grid(row=1, column=1)
ent_leader = Entry(root).grid(row=1, column=2)  # user input stored as variables

Label(root, text="# of Campers").grid(row=3, column=1)

Label(root, text="Location").grid(row=1, column=3)
ent_location = Entry(root).grid(row=1, column=4)

Label(root, text="Weather").grid(row=3, column=3)
ent_weather = Entry(root).grid(row=3, column=4)

# for grid
Label(root, text="Group").grid(row=6,column=1)
Label(root, text="Leader").grid(row=6, column=2)
Label(root, text="Campers").grid(row=6, column=3)
Label(root, text="Location").grid(row=6, column=4)
Label(root, text="Weather").grid(row=6, column=5)


# buttons >> need commands
Button(root, text="Add").grid(row=4, column=1)
Button(root, text="Delete").grid(row=4, column=2)  # add combobox in same cell
Button(root, text="View Details").grid(row=4, column=3)
Button(root, text="Quit").grid(row=4, column=4)


root.mainloop() # exclude when importing
