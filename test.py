import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = uc.Chrome()
driver.get( 'https://chat.openai.com' )

try:
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[1]"))
    )
    login_btn.click()

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("chatgpt@goodlabs.studio")
    
    continue_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "action"))
    )
    continue_btn.click()
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("y5x5UETKx6_*$v&")

    continue_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "action"))
    )
    continue_btn.click()
    
    next_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='flex gap-4 mt-6']/button"))
    )
    
    next_btn.click()

    next_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Next')]"))
    )
    
    next_btn.click()

    done_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Done')]"))
    )
    done_btn.click()
    
    chat_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    search_text = "one way to declare a variable python"
    chat_input.send_keys(search_text)
    
    submit_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea/following::button"))
    )
    submit_text.click()
    
    regenerate_response_btn = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Regenerate response')]"))
    )
    
    AI_response = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'markdown')]"))
    )
    response_text = AI_response.text
    
    print(response_text)
    # other = WebDriverWait(driver, 1000).until(
    #     EC.presence_of_element_located((By.ID, "//div[@class='flex gap-4 mt-6']/button[@class='ml-auto']"))
    # )
finally:
    driver.quit()