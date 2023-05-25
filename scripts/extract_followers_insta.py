# This code extract followers from a user to then sanitize it.

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Start the code clock
start_time = time.time()

# Get the principal webpage
time.sleep(4)
max_attempts = 5
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
username = ''
password = ""

# Decline Optional Cookies
time.sleep(5)
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
time.sleep(6)
button = browser.find_element(By.CSS_SELECTOR, "._acap > div:nth-child(1)")
button.click()

# No save the login info
time.sleep(5)
try:
	time.sleep(5)
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

# Get the User Following webpage
username2 = "ma.tempo" # -> Here you can change the target username to get all the followers.
link2 = "https://instagram.com"+username2+"/following"
browser.get(link2)
time.sleep(12)

# Create new txt file to write the output
output_string = username2 + ".txt"
with open("ma.tempo.txt", "w") as output_file: # -> Here you can change the output file name.
	# Get all the persons who is following and write it in the output
	i = 1
	print("We are in")
	for i in range(1, 12000): # You can write here how many followers do you want to scrap and select the range.
		time.sleep(1)
		try:
			parent_element = browser.find_element(By.CSS_SELECTOR, f"div.x1i10hfl:nth-child({i})")
			#browser.execute_script("arguments[0].scrollIntoView();", parent_element)

			try:
				scroll_script = "arguments[0].scrollIntoView({ behavior: 'instant' });"
				browser.execute_script(scroll_script, parent_element)
			except:
				time.sleep(1)

			if parent_element.text == "Follow":
				continue
			output_file.write(f"\n{i} -> {parent_element.text}\n")
			print("", i, " -> ", parent_element.text)
			i=i+1
		except:
			output_file.write(f"\n{i} -> {parent_element.text}\n")
			print("\n", i, " -> ")
			i=i+1
			continue

# Finish the clock
end_time = time.time()
total_time = end_time - start_time

print("Total time:", total_time, "seconds")
