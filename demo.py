import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("Command: 'Hey Siri'")
    audio = r3.listen(source)

if 'Hey Siri' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = ''
    with sr.Microphone() as source:
        print("What do you want fag?")
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("ERROR, tf you sayyy?")
        except sr.RequestError as er:
            print("ERROR")
