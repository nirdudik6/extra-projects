from selenium import webdriver
from time import sleep
from creditentials import username, password




class Instalogin:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)
        username_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username_type.send_keys(username)
        password_type = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password_type.send_keys(password)
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        submit.click()



my_bot = Instalogin(username, password)
my_bot.Instalogin()
try:
    my_bot.driver.close()
except:
    print("Fail")
    my_bot.driver.close()
