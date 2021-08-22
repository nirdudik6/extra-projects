from selenium import webdriver

print("hey what's up!!")
name = input("what's your name\n")
well = input("hello " + name + " how are you? (good/bad)\n")
if well=="good":
    print("good to hear from you!")
elif well=="bad":
    bad = input("oh no what's wrong??\n")
    print("I know what you feel but i know it'll be better soon and if you need anything so i am here for everything :)")
    fun = input("Do you feel better? (yes/ no)\n")
    if fun == "yes":
        print("good to hear :)")
    elif fun == "no":
        driver = webdriver.Chrome(executable_path=r'C:/Users/yoval/Desktop/chromedriver.exe')
        driver.get("https://www.youtube.com/watch?v=iwBTXBEN13I/")