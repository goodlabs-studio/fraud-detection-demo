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
import whisper
import torch
import numpy as np

monitors = get_monitors()

monitor_width = monitors[1].width
monitor_height = monitors[1].height

from modules.chatGPT import *
from modules.elevenlabs import *

def chat_gpt_login(driver, By, EC, WebDriverWait, username, password):
    driver.get('https://chat.openai.com')
    login_to_chat_gpt(driver, By, EC, WebDriverWait, username, password)

def elevenlabs_login(driver, By, EC, WebDriverWait, Keys, username, password):
    driver.get('https://beta.elevenlabs.io/')
    login_to_elevenlabs(driver, By, EC, WebDriverWait, Keys, username, password)

contextArray = [
    { "prompt": "You are hussain in vegas for a conference. You're on the phone with Paul", "response_type": "an appropriate", "condition": "provide a brief jolly professional response in quotes"},
    { "prompt": "You are in vegas for the nacha conference. You are on the phone with your banker", "response_type": "an appropriate one sentence", "condition": "brief light hearted response and some sentence fillers like um or uh in the sentences" },
    { "prompt": "You're in Vegas, You are following up with your banker regarding a money transfer request you sent to him earlier regarding an investment opportunity.", "response_type": "an appropriate", "condition": "and some fillers like oh, um and uh" },
    { "prompt": "you are telling your banker the reason you need the money transfer. you want to invest in a startup that you have been watching for a while. you believe the startup has potential.", "response_type": "an appropriate", "condition": " have a good reason for investing while adding some fillers like oh, um and uh" },
    { "prompt": "The amount you want to transfer is $300000.", "response_type": "an appropriate", "condition": "make the response short add some sentence fillers like uh and um" },
    { "prompt": "You are providing bank details. Provide a reinder that the account number is in the email but the last 4 digits of your account number is - 'SEVEN. - EIGHT. - EIGHT. - FOUR.'. The recepients account number is - 'NINE. - ONE. - SEVEN. - SIX.' and their bank is Bank of America", "response_type": "an appropriate", "condition": "copy the numbers as text with the periods and hyphens. add sentence fillers like uh or um" },
    { "prompt": "You're on a call with your private banker and want to wrap up the conversation.", "response_type": "an appropriate", "condition": "add sentence fillers like uh or um" },
    { "prompt": "You're on a call and want to say bye", "response_type": "an appropriate", "condition": "" },
]

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


def login(sites):    
    for site in sites:
        thread = threading.Thread(target=site["login"])
        thread.start()

    

def quit_drivers(chat_gpt_driver, resemble_ai_driver):
    chat_gpt_driver.quit()
    resemble_ai_driver.quit()

def transcribe(audio_data, audio_model, verbose=False):
    while True:
        timed_transcribe = st_time(audio_model.transcribe)
        result = timed_transcribe(audio_data)

        if not verbose:
            predicted_text = result["text"]
            return predicted_text
        else:
            return result

def listen_and_respond(chat_gpt_driver, text_to_speech_driver, ctx, audio_model):
    with sr.Microphone(sample_rate=16000) as source:    
        print("Speak...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5)
        torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
        audio_data = torch_audio
        print("Talking complete")

        acquired_text = transcribe(audio_data, audio_model)

        print(acquired_text)

        timed_ask_chat_gpt = st_time(ask_chat_gpt)
        chat_gpt_response = timed_ask_chat_gpt(chat_gpt_driver, By, EC, WebDriverWait, "Context: {}. Provide {} answer to the following {} - {}".format(ctx.get("prompt", ""), ctx.get("response_type", ""), ctx.get("condition", ""), acquired_text))

        print(chat_gpt_response)

        timed_text_to_speech = st_time(text_to_speech)
        timed_text_to_speech(text_to_speech_driver, By, EC, WebDriverWait, Keys, "{}".format(chat_gpt_response))
            
def prompt_question(chat_gpt_driver, text_to_speech_driver, audio_model):
    keep_prompting = True
    iterations = 0
    
    while (keep_prompting):
        # chat_gpt_driver.minimize_window()
        # resemble_ai_driver.minimize_window()
        ask_question = input("Press 'Y' to proceed - 'R' to reset - 'Q' to quit: ")
        if (ask_question.lower() == 'r'):
            iterations = 0

        if (ask_question.lower() == 'y'):
            timed_listen_and_respond = st_time(listen_and_respond)
            try:
                if (iterations < len(contextArray)):
                    timed_listen_and_respond(chat_gpt_driver, text_to_speech_driver, contextArray[iterations], audio_model)
                else:
                    timed_listen_and_respond(chat_gpt_driver, text_to_speech_driver, {}, audio_model)
                iterations += 1
            except:
                print("Something went wrong")
        
        if (ask_question.lower() == 'q'):
            print("Quitting...")
            keep_prompting = False
            quit_drivers(chat_gpt_driver, text_to_speech_driver)

if __name__ == "__main__":
    load_dotenv()
    r = sr.Recognizer()

    # MODELS: can be ["tiny","base", "small","medium","large"]
    audio_model = whisper.load_model("small")
    
    # ChatGPT setup
    chat_gpt_username = os.getenv('CHATGPT_USERNAME')
    chat_gpt_password = os.getenv('CHATGPT_PASSWORD')

    # ResembleAI setup
    # resemble_ai_username = os.getenv('RESEMBLEAI_USERNAME')
    # resemble_ai_password = os.getenv('RESEMBLEAI_PASSWORD')
    # resemble_ai_project = os.getenv('RESEMBLEAI_PROJECT')
    # resemble_ai_clip = os.getenv('RESEMBLEAI_CLIP')
    
    # ResembleAI setup
    elevenlabs_username = os.getenv('ELEVENLABS_USERNAME')
    elevenlabs_password = os.getenv('ELEVENLABS_PASSWORD')

    # TODO: create setup script for all drivers that takes into account the number of drivers and positions them.
    chat_gpt_driver = uc.Chrome(version_main = 112)
    chat_gpt_driver.set_window_size(monitor_width/2, monitor_height)
    chat_gpt_driver.set_window_position(-monitor_width/2, 0)

    elevenlabs_driver = uc.Chrome(version_main = 112)    
    elevenlabs_driver.set_window_size(monitor_width/2, monitor_height)
    elevenlabs_driver.set_window_position(-monitor_width, 0)

    sites = [
        {
            'login': chat_gpt_login(chat_gpt_driver, By, EC, WebDriverWait, chat_gpt_username, chat_gpt_password)
        },
        {
            'login': elevenlabs_login(elevenlabs_driver, By, EC, WebDriverWait, Keys, elevenlabs_username, elevenlabs_password)
        }
    ]


    # login(sites)
    prompt_question(chat_gpt_driver, elevenlabs_driver, audio_model)