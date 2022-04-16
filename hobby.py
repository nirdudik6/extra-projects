from tkinter import *
from selenium import webdriver
from time import sleep
import os

def runescape():
    sleep(1)
    os.system(#program link)
    window.destroy()
    exit()

def trading():
    window.destroy()
    sleep(1)
    driver = webdriver.Chrome(#chromedriver link)
    driver.get("https://tradingview.com")
    window.destroy()


def close_window():
    window.destroy()
    exit()

print("hello welcome to my hobby project!")
window = Tk()
window.geometry("1600x600")
window.title("MAIN")
window.configure(background="black")

Label(window, text="\nWELCOME TO MY HOBBY PROJECT MENU! :)", width=60, bg="black", fg="white", font="verdana 30 italic").grid(row=1, column=0, sticky='W')
Label(window, text="\n\n\nEnter you choice:\n1.runescape\n2.trading\n", width=60,bg="black", fg="white", font="verdana 30 italic").grid(row=7, column=0, sticky='W')

Button(window, text="Runescape", width=30, command=runescape, font="none 12 italic").grid(row=9, column=0, sticky=S)
Button(window, text="trading", width=30, command=trading, font="none 12 italic").grid(row=11, column=0, sticky=S)
Button(window, text="EXIT", width=30, command=close_window, font="none 12 italic").grid(row=13, column=0, sticky=S)

window.mainloop()

