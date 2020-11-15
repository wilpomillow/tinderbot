# Import packages
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from pyautogui import click, PAUSE, confirm, FAILSAFE, press, position, moveTo, moveRel, typewrite, keyDown, keyUp, locateCenterOnScreen, screenshot, hotkey
from time import sleep
from random import randint, random
import webbrowser
import csv

print('Packages imported successfully.')

# Activate failsafe early in case something goes wrong
FAILSAFE = True

# Initiate web browser
# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--incognito")
# driver = webdriver.Chrome(chrome_options=options)

# Navigate to Tinder homepage
#driver.get("https://tinder.com/?lang=en-US")

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
webbrowser.get(chrome_path).open('https://tinder.com/?lang=en-US')

# This will help us find things on the screen to click with 90% confidence
def screen_click(button_image):
    button = locateCenterOnScreen(button_image)
    if not button:
        print(button_image + ' was not found')
    else:
        click(button)
        print(button_image + ' found')

# Reactions for if we want to swipe left (reject) or right (accept)
def reject():
    time = randint(0,2) + round(random(),2)
    sleep(time)
    press('left')

def like():
    time = randint(0,2) + round(random(),2)
    sleep(time)
    press('right')
sleep(12)

relax = 1
breathe = 2

# Tinder values our privacy but it takes up screen space so let's get rid of it
screen_click('personalize.png')
sleep(breathe)
screen_click('refuse.png')
sleep(breathe)
screen_click('options.png')
sleep(relax)
screen_click('login.png')
sleep(relax)
screen_click('options.png')
moveRel(200,-50)
sleep(relax)
screen_click('facebook.png')
sleep(breathe)

counter = 0
# with open('log_in.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for column in csv_reader:
#         if counter == 0:
#             usr = column[0]
#             counter += 1
#         else:
#             pwd = column[0]

# sleep(relax)

# if locateCenterOnScreen('minifacebook.png'):
#     press('tab')
# else:
#     print('Logging in')


# typewrite(usr)
# press('tab')
# typewrite(pwd)

sleep(relax)
# begin = confirm(text='Begin TinderBot?', title='TinderBot Execute', buttons=['OK', 'Cancel'])
# if begin == 'OK':
#     sleep(0.2)
#     screen_click('facebook_login.png')



