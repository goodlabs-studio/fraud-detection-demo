def text_to_speech(driver, By, EC, WebDriverWait, Keys, username, password, project, clip, paragraph):
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[email]"))
    )
    username_input.send_keys(username)
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[password]"))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # TODO: Replace the action value with the value for the clip of the person we want
    project_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form[@action='/projects/{}/clips']/input[@value='Clips']".format(project)))
    )
    
    project_btn.click()
    
    # TODO: Replace the action value with the value for the clip of the person we want
    recording_path = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/projects/{}/clips/{}']".format(project, clip)))
    )
    
    recording_path.click()
    
    word_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@data-slate-leaf="true"]'))
    )
    
    print(paragraph)
    # word_input.send_keys(u'\ue009' + u'\ue003')
    word_input.send_keys(paragraph)

    # driver.switch_to.active_element.send_keys("TEST")
    
    generate_and_speak_btn = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.ID, "segment-0-generate"))
    )
    generate_and_speak_btn.click()


    elem = WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.ID, "//div[contains(text(), 'Write here...')]"))
    )
