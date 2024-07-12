# Project NiceShot (NLP Processing)
# Created : 2024.07.10 By Mint
# Last Modified :
# Dev Stage : TP1

import settings
import speech_recognition as sr
import papago

settings.setup()

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("듣는중..")
        voice = recognizer.listen(source)
        vtt = recognizer.recognize_google(voice, language=settings.lang)
        print(vtt)
        if settings.papago_enabled == 1:
            print("번역 결과입니다.")
            print(papago.translate(vtt, settings.lang.split("-")[0], "ko"))
except:
    print("인식할 수 없습니다.")