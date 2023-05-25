# This code creates 5 bots listed in the 'file_name' txt file.
# The automate browser start the CHAT with BotFather and creates more bots.

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()

browser.get('https://web.telegram.org/k/')
time.sleep(5)

# First click
button = browser.find_element(By.XPATH, "//button[contains(.,'Log in by phone Number')]")
button.click()


# Find the phone number input field by class name and enter the phone number
phone_input = browser.find_element(By.CSS_SELECTOR, ".input-field.input-field-phone > div")
phone_input.send_keys("+52 ") # -> Your complete phone number goes here

page_source = browser.page_source
#print(page_source)
with open("Telegram1.html", "w") as file:
	file.write(page_source)

# Second click
button = browser.find_element(By.XPATH, "//button[contains(.,'Next')]")
button.click()

# Enter the manual code
print("Write the manual code: ")
code = input()
time.sleep(3)
code_container = browser.find_element(By.CSS_SELECTOR, 'input.input-field-input')
code_container.send_keys(code)

# Check if there exists a Master Password
time.sleep(3)
try:
	master_container = browser.find_element(By.CSS_SELECTOR, 'input.input-field-input:nth-child(2)')
	print("Write the master password: ")
	master_password = input()
	master_container.send_keys(master_password)
	next_buttom = browser.find_element(By.CSS_SELECTOR, 'button.btn-primary:nth-child(2) > div:nth-child(1)')
	next_buttom.click()
except NoSuchElementException:
                        pass

# Write "BotFather"
time.sleep(3)
search_container = browser.find_element(By.CSS_SELECTOR, '.input-field-input')
search_container.send_keys("BotFather")

# Select "BotFather" chat
time.sleep(2)
bot_container = browser.find_element(By.CSS_SELECTOR, 'div.search-group:nth-child(1) > ul:nth-child(2) > a:nth-child(1) > div:nth-child(1)')
bot_container.click()

i = 0
times = [2, 5, 280, 5, 280]

file_name = "bots23.txt" # -> The name of your filename goes here.
with open(file_name, 'r') as f:
	for line in f:
		# Respective Sleep
		x = times[i]
		#time.sleep(x)
		i=i+1
		for j in range(1,x+1):
                        print(j)
                        time.sleep(1)

		# Start the chat with BotFather
		search_container = browser.find_element(By.CSS_SELECTOR, 'div.input-message-input:nth-child(1)')
		search_container.send_keys("/newbot")
		search_container.send_keys(Keys.ENTER)

		# Name the Bot
		time.sleep(2)
		search_container = browser.find_element(By.CSS_SELECTOR, 'div.input-message-input:nth-child(1)')
		search_container.send_keys(line.strip())
		search_container.send_keys(Keys.ENTER)

		# Username the Bot
		time.sleep(2)
		search_container = browser.find_element(By.CSS_SELECTOR, 'div.input-message-input:nth-child(1)')
		search_container.send_keys(line.strip())
		search_container.send_keys(Keys.ENTER)

		# Error Message1
		time.sleep(2)
		try:
			sorry_message1 = browser.find_element(By.XPATH, '//div[contains(text(),"Sorry, this username is already taken.")]')
			if sorry_message1.text == "Sorry, this username is already taken. Please try something different.":
				print("flag! Repeated")
				i=i-1
		except NoSuchElementException:
			pass

		# Error Message2
		time.sleep(2)
		try:
			last_answer = browser.find_elements(By.XPATH, '//div[last()]')
			if last_answer and "Sorry, too many attempts." in last_answer[-1].text:
				delay = int(re.search(r"\d+", last_answer[-1].text).group())
				print("Too many attempts. Sleeping for {delay} seconds.")
				time.sleep(delay)
				i -= 1
		except NoSuchElementException:
			pass

		# Error Message3
		time.sleep(2)
		try:
			sorry_message3 = browser.find_element(By.XPATH, '//div[contains(text(),"I can help you create and manage Telegram bots.")]')
			if "Bot API" in sorry_message3.text:
				print(f"Flag 2")
				time.sleep(2)
		except NoSuchElementException:
				pass


		# Save the Token
		#token = browser.find_element(By.CSS_SELECTOR, 'div.bubbles-group:nth-child(31) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > code:nth-child(3)')
			#with open('token.txt', 'w') as f:
				#f.write(token.text)

#browser.quit()
