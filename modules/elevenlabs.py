def login_to_elevenlabs(driver, By, EC, WebDriverWait, Keys, username, password):    
    sign_in_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Sign in')]"))
    )
    sign_in_btn.click()
    
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    username_input.send_keys(username)
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

def text_to_speech(driver, By, EC, WebDriverWait, Keys, paragraph):    
    word_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "text"))
    )
    
    # change to Keys.CONTROL if not on mac
    word_input.send_keys(Keys.COMMAND, "a")
    word_input.send_keys(paragraph)

    # driver.switch_to.active_element.send_keys("TEST")
    
    generate_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Generate')]"))
    )
    generate_btn.click()

