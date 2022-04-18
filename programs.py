from tkinter import *
import os
from time import sleep

def TEAMS():
    sleep(1)
    os.system('C:/Users/nird/AppData/Local/Microsoft/Teams/current/Teams')
    window.destroy()
    exit()



def SPOTIFY():
    sleep(1)
    os.system('C:/Users/nird/AppData/Roaming/Spotify/Spotify')
    window.destroy()
    exit()


def close_window():
    window.destroy()
    exit()

window = Tk()
window.geometry("1600x800")
window.title("MAIN")
window.configure(background="black")

Label(window, text="\nWELCOME! :)", width=60, bg="black", fg="white", font="verdana 30 italic").grid(row=1, column=0, sticky='W')
Label(window, text="\n\n\nEnter you choice:\n\n\n", width=60,bg="black", fg="white", font="verdana 30 italic").grid(row=7, column=0, sticky='W')

Button(window, text="TEAMS", width=30, command=TEAMS, font="none 12 italic").grid(row=9, column=0, sticky=S)
Button(window, text="SPOTIFY", width=30, command=SPOTIFY, font="none 12 italic").grid(row=11, column=0, sticky=S)
Button(window, text="EXIT", width=30, command=close_window, font="none 12 italic").grid(row=13, column=0, sticky=S)

window.mainloop()