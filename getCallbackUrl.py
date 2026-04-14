#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from urllib import parse
import webbrowser
import json
import os
import sys

folder_dir = str(sys.argv[1])
print (folder_dir + "\n")

email = str(sys.argv[2])
print (email + "\n")

password = str(sys.argv[3])
print (password + "\n")


url = " https://login.microsoftonline.com/<Application tenant id for the app registered on Azure portal>/oauth2/v2.0/authorize?client_id=<Application client id for the app registered on Azure portal>&response_type=code&response_mode=query&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default&state=12345"

driver = webdriver.Chrome()

driver.get(url)
sleep(10)

elem = driver.find_element(By.NAME, "loginfmt")

elem.send_keys(email)
sleep (1)
elem.send_keys(Keys.RETURN)

sleep (5)
elem = driver.find_element(By.NAME, "passwd")

elem.send_keys(password)
sleep (1)
elem.send_keys(Keys.RETURN)

sleep (5)

get_url = driver.current_url

sleep(3)


print(driver.current_url)

auth_url = driver.current_url
auth_response = dict(parse.parse_qsl(parse.urlsplit(auth_url).query))
print ("\n")
print (auth_response)
print (json.dumps(auth_response))


folder_path = folder_dir
file_name = 'auth_code.json'

full_name = os.path.join(folder_path,file_name)

print ("\n")
print (full_name)

with open(full_name, 'w') as jsonout:
    jsonout.write(json.dumps(auth_response))


auth_code = auth_response.get('code')
print ("\n")
print (auth_code)
driver.close()
