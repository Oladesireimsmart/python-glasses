# ================================
# LETTER WRITING APPLICATION
# ================================

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


# ---------- PART 1: the main window ----------
# YOUR CODE HERE
# Create the window with Tk(), give it a title and a geometry of "600x500".
# Then configure row 0 and column 1 with weight=1 so the editor stretches
# when the window is resized. Read the note in the Instructions about why
# it is column 1 and not column 0.


# ---------- PART 2: open an existing letter ----------
# YOUR CODE HERE
# def open_letter():
#     ask the user to pick a file, offering Text Files (*.txt) and All Files
#     if they cancelled, stop the function with a bare  return
#     clear the editor from 1.0 to END
#     open the file in read mode, read() it, insert it at END
#     update the window title to show the filepath


# ---------- PART 3: save the letter under a new name ----------
# YOUR CODE HERE
# def save_letter():
#     ask the user where to save, with defaultextension=".txt"
#     if they cancelled, stop the function
#     open the chosen path in write mode
#     get() the editor's text from 1.0 to END and write() it
#     update the window title


# ---------- PART 4: the widgets ----------
# YOUR CODE HERE
# A Text widget called txt_edit.
# A Frame called fr_buttons, with relief=RAISED and bd=2.
# Two Buttons inside that frame: "Open Letter" and "Save Letter As..."
# Give each one  command=  the matching function — NO parentheses.


# ---------- PART 5: lay it out with grid ----------
# YOUR CODE HERE
# btn_open   -> row 0, column 0 of the frame, sticky "ew"
# btn_save   -> row 1, column 0 of the frame, sticky "ew"
# fr_buttons -> row 0, column 0 of the window, sticky "ns"
# txt_edit   -> row 0, column 1 of the window, sticky "nsew"


# ---------- PART 6: start the program ----------
# YOUR CODE HERE
# One line. Without it the window is created but doesn't run.