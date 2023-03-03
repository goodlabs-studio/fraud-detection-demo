import os
import time
import threading
import speech_recognition as sr
import undetected_chromedriver as uc
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from screeninfo import get_monitors

monitors = get_monitors()

monitor_width = monitors[1].width
monitor_height = monitors[1].height

from modules.chatGPT import *
from modules.resembleAI import *

def st_time(func):
    """
        st decorator to calculate the total time of a func
    """

    def st_func(*args, **keyArgs):
        t1 = time.time()
        r = func(*args, **keyArgs)
        t2 = time.time()
        print("Function=%s, Time=%s" % (func.__name__, t2 - t1))
        return r

    return st_func


def login(chat_gpt_driver, chat_gpt_username, chat_gpt_password, resemble_ai_username, resemble_ai_password, resemble_ai_project):
    def chat_gpt_login():
        chat_gpt_driver.get('https://chat.openai.com')
        login_to_chat_gpt(chat_gpt_driver, By, EC, WebDriverWait, chat_gpt_username, chat_gpt_password)
    
    def resemble_ai_login():
        resemble_ai_driver.get( 'https://app.resemble.ai')
        login_to_resemble_AI(resemble_ai_driver, By, EC, WebDriverWait, Keys, resemble_ai_username, resemble_ai_password, resemble_ai_project)

    login_thread_1 = threading.Thread(target=chat_gpt_login)
    login_thread_1.start()
    
    login_thread_2 = threading.Thread(target=resemble_ai_login)
    login_thread_2.start()

    

def quit_drivers(chat_gpt_driver, resemble_ai_driver):
    chat_gpt_driver.quit()
    resemble_ai_driver.quit()

def listen_and_respond(chat_gpt_driver, resemble_ai_driver, resemble_ai_project, resemble_ai_clip):
    with sr.Microphone() as source:    
        print("Speak...")
        # listen(
        #     source,
        #     timeout,
        #     phrase_time_limit,
        #     snowboy_configuration
        # )
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5)
        print("Talking complete")
        
        timed_recognize = st_time(r.recognize_google)
        acquired_text = timed_recognize(audio)
    
        # Bring window forward
        chat_gpt_driver.switch_to.window(chat_gpt_driver.current_window_handle)
        resemble_ai_driver.switch_to.window(resemble_ai_driver.current_window_handle)

        timed_ask_chat_gpt = st_time(ask_chat_gpt)
        chat_gpt_response = timed_ask_chat_gpt(chat_gpt_driver, By, EC, WebDriverWait, "improv with me in one sentence {}".format(acquired_text))

        timed_text_to_speech = st_time(text_to_speech)
        timed_text_to_speech(resemble_ai_driver, By, EC, WebDriverWait, Keys, resemble_ai_project, resemble_ai_clip, chat_gpt_response)
            
def prompt_question(chat_gpt_driver, resemble_ai_driver, resemble_ai_project, resemble_ai_clip):
    keep_prompting = True
    
    while (keep_prompting):
        # chat_gpt_driver.minimize_window()
        # resemble_ai_driver.minimize_window()
        ask_question = input("Press 'Y' to ask or 'Q' to quit: ")
        if (ask_question.lower() == 'y'):
            timed_listen_and_respond = st_time(listen_and_respond)
            try:
                timed_listen_and_respond(chat_gpt_driver, resemble_ai_driver, resemble_ai_project, resemble_ai_clip)
            except:
                print("Something went wrong")
        
        if (ask_question.lower() == 'q'):
            print("Quitting...")
            keep_prompting = False
            quit_drivers(chat_gpt_driver, resemble_ai_driver)

if __name__ == "__main__":
    load_dotenv()
    r = sr.Recognizer()
    
    # ChatGPT setup
    chat_gpt_username = os.getenv('CHATGPT_USERNAME')
    chat_gpt_password = os.getenv('CHATGPT_PASSWORD')

    # ResembleAI setup
    resemble_ai_username = os.getenv('RESEMBLEAI_USERNAME')
    resemble_ai_password = os.getenv('RESEMBLEAI_PASSWORD')
    resemble_ai_project = os.getenv('RESEMBLEAI_PROJECT')
    resemble_ai_clip = os.getenv('RESEMBLEAI_CLIP')

    chat_gpt_driver = uc.Chrome()
    chat_gpt_driver.set_window_size(monitor_width/2, monitor_height)
    chat_gpt_driver.set_window_position(-monitor_width/2, 0)

    resemble_ai_driver = uc.Chrome()    
    resemble_ai_driver.set_window_size(monitor_width/2, monitor_height)
    resemble_ai_driver.set_window_position(-monitor_width, 0)

    login(chat_gpt_driver, chat_gpt_username, chat_gpt_password, resemble_ai_username, resemble_ai_password, resemble_ai_project)
    prompt_question(chat_gpt_driver, resemble_ai_driver, resemble_ai_project, resemble_ai_clip)