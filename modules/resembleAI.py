def login_to_resemble_AI(driver, By, EC, WebDriverWait, Keys, username, password, project):    
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[email]"))
    )
    username_input.send_keys(username)
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[password]"))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@action='/projects/{}/clips']/input[@value='Clips']".format(project)))
    )

def text_to_speech(driver, By, EC, WebDriverWait, Keys, project, clip, paragraph):    
    driver.get('https://app.resemble.ai/projects/{}/clips/{}'.format(project, clip))
    
    word_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-slate-leaf="true"]'))
    )
    
    # trying to clear the input before typing
    # word_input.send_keys(u'\ue009' + u'\ue003')
    word_input.click()
    word_input.send_keys(Keys.CONTROL + "a")
    word_input.send_keys(Keys.BACKSPACE)
    word_input.send_keys(paragraph)

    # driver.switch_to.active_element.send_keys("TEST")
    
    generate_and_speak_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "segment-0-generate"))
    )
    generate_and_speak_btn.click()

    # when the stop btn appears we usually have the audio playing
    stop_btn = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-icon="pause"]'))
    )

