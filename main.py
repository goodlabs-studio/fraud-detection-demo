import os
from dotenv import load_dotenv

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import speech_recognition as sr

from chatGPT import *
from resembleAI import *


load_dotenv()
r = sr.Recognizer()

print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
    print("Talk")
    # listen(
    #     source,
    #     timeout,
    #     phrase_time_limit,
    #     snowboy_configuration
    # )
    audio = r.listen(source, 10)
    print("Talking complete")

    driver = uc.Chrome()
    
    try:
        acquired_text = r.recognize_google(audio)
        print(acquired_text)
        # ChatGPT setup
        username = os.getenv('CHATGPT_USERNAME')
        password = os.getenv('CHATGPT_PASSWORD')

        driver.get('https://chat.openai.com')

        chat_gpt_response = ask_chat_gpt(driver, By, EC, WebDriverWait, username, password, "improv with me in one sentence {}".format(acquired_text))

        # ResembleAI setup
        username = os.getenv('RESEMBLEAI_USERNAME')
        password = os.getenv('RESEMBLEAI_PASSWORD')
        project = os.getenv('RESEMBLEAI_PROJECT')
        clip = os.getenv('RESEMBLEAI_CLIP')

        driver.get( 'https://app.resemble.ai')
        text_to_speech(driver, By, EC, WebDriverWait, Keys, username, password, project, clip, chat_gpt_response)
    finally:
        driver.quit()

