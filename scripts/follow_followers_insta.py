# This code follows the list of instagram users provided initially.
# Optionally, you can scroll the webpage until the time.sleep(350) get finished.

import time
import re
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Start the code clock
start_time = time.time()

# Get the principal webpage
time.sleep(1)
max_attempts = 2
attempt_count = 0
browser = None
while attempt_count < max_attempts:
        try:
                time.sleep(1)
                browser = webdriver.Firefox()
                browser.get('https://instagram.com')
                break
        except:
                attempt_count += 1
                print(f"Attempt {attempt_count} failed. Retrying...")
                time.sleep(1)

# Your Credentials Go Here
username = 'xxxxx'
password = "xxxxx"

# Decline Optional Cookies
time.sleep(1)
max_attempts = 2
attempt_count = 0
while attempt_count < max_attempts:
	try:
		button = browser.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(3)")
		button.click()
	except:
		attempt_count += 1
		print(f"Attempt {attempt_count} failed. Retrying...")
		time.sleep(1)

# Input the username
time.sleep(1)
username_input = browser.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
username_input.send_keys(username)

# Input the password
time.sleep(1)
password_input = browser.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
password_input.send_keys(password)

# Log In - Click
time.sleep(1)
button = browser.find_element(By.CSS_SELECTOR, "._acap > div:nth-child(1)")
button.click()

# No save the login info
time.sleep(1)
try:
	button = browser.find_element(By.CSS_SELECTOR, "div.x1i10hfl")
	button.click()
except:
	print("continue")

# Turn Notifications Off
time.sleep(5)
max_attempts = 2
attempt_count = 0
while attempt_count < max_attempts:
	try:
		button = browser.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(2)")
		button.click()
	except:
		attempt_count += 1
		print(f"New Attempt {attempt_count} failed. Retrying...")
		time.sleep(1)
cont1 = 1
cont2 = 1
button_value = False

# You need to write here the name of the 'sanitized output file'
with open("sanitized_ma.tempo.txt", "r") as input_file:
	for username in input_file:
		min_user = 1
		max_user = 200
		if cont1 in range(min_user, max_user):
			link_username = 'https://instagram.com/' + username
			browser.get(link_username)
			time.sleep(3)

			# numerate all the selector and iterate it. You can add more if you need.
			css_selectors = [
				"div._aaco",
				"div._aacw",
				"._acan",
				"div._aaco",
				".x150jy0e",
				"div._aaco",
				".x150jy0e > div:nth-child(2) > span:nth-child(1) > svg:nth-child(1)",
				".x150jy0e > div:nth-child(2) > span:nth-child(1) > svg:nth-child(1)",
				"._acat > div:nth-child(1) > div:nth-child(1)",
				".x150jy0e > div:nth-child(1)"
			]

			try:
				for css_selector in css_selectors:
					button = browser.find_element(By.CSS_SELECTOR, css_selector)
					if button.text == "Following" or button.text == "Requested":
						print(f"Already followed or requested this <{css_selector}> -> {username}")
						cont2 = cont2 + 1
						break
					else:
						sleep(3)
						button.click()

						# Make other actions while there exists another call
						print(cont2+min_user, " -> ", username)
						cont2 = cont2 + 1
						#browser.get('https://instagram.com/')
						for j in range(1, 350):
							print(j)
							time.sleep(1)

						# This part is optional, you can scroll the principal web page with it.
						"""
						try:
							# Scroll down the page
							body = browser.find_element(By.TAG_NAME, 'body')
							for i in range(random.randint(1, 2)):
								#time.sleep(random.uniform(1,2))
								body.send_keys(Keys.PAGE_DOWN)
								#continue
							time.sleep(1)
						except:
							time.sleep(1)
						"""

			except:
				# The except beggin with another try to prove
				try:
					button = browser.find_element(By.CSS_SELECTOR, css_selector)
					if button.text == "Following" or button.text == "Requested":
						print(f"Already followed or requested this <{css_selector}> -> {username}")
						break
					button.click()
					butto_value = True

					# Make other actions while there exists another call
					print(cont2+min_user, " -> ", username)
					cont2 = cont2 + 1
					#browser.get('https://instagram.com/')
					for j in range(1, 350):
						print(j)
						time.sleep(1)

				except:
					continue
					print(f"Can't found the <{css_selector}> of this -> {username}")
					css_selector_new = input("Give the correct CSS: ")
					css_selectors.append(css_selector_new)
					try:
						button = browser.find_element(By.CSS_SELECTOR, css_selector_new)
						if button.text == "Following" or button.text == "Requested":
							print("Already followed or requested -> ", username)
							continue
						button.click()
					except:
						continue
		else:
			cont1 = cont1 + 1
