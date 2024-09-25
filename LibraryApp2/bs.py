from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (the path can be omitted if in /usr/local/bin)
service = Service('/usr/local/bin/chromedriver')  # Adjust this if needed
driver = webdriver.Chrome(service=service)

try:
    # Open the webpage with the accordion
    driver.get('https://www.tbcacademy.ge/usaid/python-advance')

    # Wait for the button to be clickable
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h3[@id='title_5']/parent::div/parent::div/button"))
    )
    button.click()

    # Optional: wait to see the result
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()
