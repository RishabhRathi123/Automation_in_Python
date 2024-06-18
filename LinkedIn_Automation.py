from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to LinkedIn
driver.get("https://www.linkedin.com/login")

# Function to perform login
def linkedin_login(email, password):
    # Find the username field and input the email
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(email)
    
    # Find the password field and input the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    
    # Find the login button and click it
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

# Replace these with your LinkedIn login credentials
email = "your_email@example.com"
password = "your_password"

# Perform the login
linkedin_login(email, password)

# Wait for a few seconds to ensure the login is complete
time.sleep(5)

# Perform additional tasks here
# For example: Searching for jobs
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_bar.send_keys("Software Engineer")
search_bar.send_keys(Keys.RETURN)

# Wait for a few seconds to observe the results
time.sleep(5)

# Always remember to close the browser after automation tasks
driver.quit()
