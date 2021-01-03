from selenium import webdriver
from time import sleep
from tkinter import *


def instagram():
    def instagram_login():
        class InstaUnfollowers:
            def __init__(self, username, password):
                self.driver = webdriver.Chrome()
                self.driver.get("https://instagram.com")
                sleep(2)
                # instagram login
                username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
                username_type.send_keys(username)
                password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
                password_type.send_keys(password)
                submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
                submit.click()

        username = textentry1.get()
        password = textentry2.get()
        my_bot = InstaUnfollowers(username,password)
        my_bot.get_unfollowers()
        try:
            my_bot.driver.close()
        except:
            print("Fail")
            my_bot.driver.close()


    window = Tk()
    window.geometry("1600x900")
    window.title("instagram")
    window.configure(background="red")

    Label(window, text="\nwelcome to instagram login", width=60, bg="red", fg="black", font="verdana 30 italic").grid(row=6, column=0, sticky='W')
    Label(window, text="\n\n\nEnter your username:", width=60, bg="red", fg="black", font="verdana 30 italic").grid(row=7, column=0, sticky='W')
    textentry1 = Entry(window, width=40, bg="white", font="none 15 italic")
    textentry1.grid(row=8, column=0, sticky=S)
    Label(window, text="\nEnter your password:", width=60, bg="red", fg="black", font="verdana 30 italic").grid(row=9, column=0, sticky='W')
    textentry2 = Entry(window, width=40, bg="white", font="none 15 italic")
    textentry2.grid(row=10, column=0, sticky=S)
    Button(window, text="SUBMIT", width=25, command=instagram_login, font="none 12 italic").grid(row=11, column=0, sticky=S)
    Button(window, text="EXIT", width=25, command=close_window, font="none 12 italic").grid(row=12, column=0, sticky=S)

    window.mainloop()



def facebook():
    class InstaUnfollowers:
        def __init__(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://facebook.com")
            sleep(2)
            username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            username_type.send_keys()
            password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            password_type.send_keys()
            submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
            submit.click()


    my_bot = InstaUnfollowers()
    my_bot.get_unfollowers()
    try:
        my_bot.driver.close()
    except:
        print("Fail")
        my_bot.driver.close()

def whatsapp():
    driver = webdriver.Chrome(executable_path=r'')
    driver.get("https://web.whatsapp.com/")

def close_window():
    window.destroy()
    exit()

window = Tk()
window.geometry("1600x900")
window.title("social network project")
window.configure(background="light blue")


Label(window, text="\nWELCOME TO MY SOCIAL NETWORK PROJECT MENU! :)", width=60, bg="light blue", fg="black", font="verdana 30 italic").grid(row=1, column=0, sticky='W')
Label(window, text="\n\n\nEnter you choice:\n", width=60, bg="light blue", fg="black", font="verdana 30 italic").grid(row=7, column=0, sticky='W')


Button(window, text="login instagram", width=25, command=instagram, font="none 12 italic").grid(row=11, column=0, sticky=S)
Button(window, text="login facebook", width=25, command=facebook, font="none 12 italic").grid(row=12, column=0, sticky=S)
Button(window, text="send message in whatsapp", width=25, command=whatsapp, font="none 12 italic").grid(row=13, column=0, sticky=S)
Button(window, text="EXIT", width=25, command=close_window, font="none 12 italic").grid(row=14, column=0, sticky=S)

window.mainloop()
