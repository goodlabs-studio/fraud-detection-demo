def ask_chat_gpt(driver, By, EC, WebDriverWait, username, password, search_text):
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[1]"))
    )
    login_btn.click()

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys(username)
    
    continue_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "action"))
    )
    continue_btn.click()
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(password)

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
    
    return response_text
