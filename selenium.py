from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get('https://juliansimon.com')
text = driver.find_element(By.TAG_NAME, 'body').text
with open('output.txt', 'w') as f:
    f.write(text)
driver.quit()

