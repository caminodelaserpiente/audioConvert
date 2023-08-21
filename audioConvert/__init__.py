"""
Author: 蛇道
Url: https://github.com/caminodelaserpiente
"""


import os

from audioConvert.audio_to_text.audio_to_text import *


def banner():
    banner= """
        _                _  _           ____                                   _   
       / \    _   _   __| |(_)  ___    / ___|  ___   _ __  __   __  ___  _ __ | |_ 
      / _ \  | | | | / _` || | / _ \  | |     / _ \ | '_ \ \ \ / / / _ \| '__|| __|
     / ___ \ | |_| || (_| || || (_) | | |___ | (_) || | | | \ V / |  __/| |   | |_ 
    /_/   \_\ \__,_| \__,_||_| \___/   \____| \___/ |_| |_|  \_/   \___||_|    \__| \n"""
    print(banner)


def option_file():
    options = {
        0: 'bye',
        1: '.mp3',
        2: '.mp4'
    }
    menu = f""" 
    ----------------------------------------------------
        - Select type file to convert. (e.g. >>> 1)
            [0] {options[0]}
            [1] {options[1]}
            [2] {options[2]}"""
    print(menu)
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = int(input("Select option.\n>>> "))
            if response in options.keys():
                return response
            else:
                print("[Error] Please enter a valid option.\n")
                attempts += 1
        except ValueError:
            attempts += 1
            print("[Error] Please enter a valid numerical option.\n")
    print("Exceeded maximum attempts. Exiting the program.")
    exit()


def option_convert():
    options = {
        1: 'Text transcription (.txt)',
        2: 'Creation of subtitles (.sbv)'
    }
    menu = f"""
    ----------------------------------------------------
        - Select option to convert. (e.g. >>> 2)
            [1] {options[1]}
            [2] {options[2]}"""
    print(menu)
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = int(input("Select option.\n>>> "))
            if response in options.keys():
                return response
            else:
                print("[Error] Please enter a valid option.\n")
                attempts += 1
        except ValueError:
            attempts += 1
            print("[Error] Please enter a valid numerical option.\n")
    print("Exceeded maximum attempts. Exiting the program.")
    exit()


def audioConvert():
    banner()
    model = model_whisper()
    try:
        while True:
            response = option_file()
            if response == 0:
                print('bye')
                break
            elif response == 1:
                response = option_convert()
                path = get_path_mp3()
                audio_convert(response, model, path)
            elif response == 2:
                response = option_convert()
                path = get_path_mp4()
                path_audio = video_to_audio(path)
                audio_convert(response, model, path_audio)
    except KeyboardInterrupt:
        print("\ninterrupted by the user bye")
        