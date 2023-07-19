# importing module
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome('C:\\Users\\Darknet\\Downloads\\Compressed\\chromedriver.exe')
service = Service('C:\\Users\\Darknet\\Downloads\\Compressed\\chromedriver.exe')

service.start()
driver = webdriver.Remote(service.service_url)
# enter receiver user name
user = ['animeislv']
message_ = ("final test")


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

		# first pop-up
        self.bot.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(5)

		# 2nd pop-up
        self.bot.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(5)

		# direct button
        self.bot.find_element(by=By.XPATH, value='//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(5)

		# clicks on pencil icon
        self.bot.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(5)
        for i in user:

			# enter the username
            self.bot.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(5)

			# click on the username
            self.bot.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[2]/div[2]/div').click()
            time.sleep(5)

			# next button
            self.bot.find_element(by=By.XPATH, value='/html/body/div[4]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(5)

			# click on message area
            send = self.bot.find_element(by=By.XPATH, value='/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

			# types message
            send.send_keys(self.message)
            time.sleep(5)

			# send message
            send.send_keys(Keys.RETURN)
            time.sleep(5)

			# clicks on direct option or pencl icon
            self.bot.find_element(by=By.XPATH, value='/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(5)


def init():
    bot('uranus07_milkeyway', 'Arun@1234', user, message_)

	# when our program ends it will show "done".
    input("DONE")


# calling the function
#init()
u = "uranus07_milkeyway"
p = "Arun@1234"
url = 'https://instagram.com/'+'astha_patel_24'
driver.get("https://www.instagram.com/accounts/login/?next=/astha_patel_24/")
time.sleep(4)
#log_but = driver.find_element_by_class_name("L3NKy")
#time.sleep(5)
#log_but.click()
time.sleep(4)
usern = driver.find_element_by_name("username")
usern.send_keys(u)
passw = driver.find_element_by_name("password")
passw.send_keys(p)
passw.send_keys(Keys.RETURN)
time.sleep(5.5)
notk = driver.find_element_by_class_name("yWX7d") 
notk.click()
time.sleep(3)
message = driver.find_element_by_class_name('_aade ')
message.click()
time.sleep(2)
#notk = driver.find_element_by_class_name("_a9_1")
#notk.click()
#time.sleep(3)
#driver.find_element_by_class_name('HoLwm ').click()
time.sleep(10)
mbox = driver.find_element_by_tag_name('textarea')
#mbox = driver.find_element_by_class_name("_abbh") 
for i in range(300):
    mbox.send_keys("Ummmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhh")
    mbox.send_keys(Keys.RETURN)
    time.sleep(2)
    
