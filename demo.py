import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pyt

r1 = sr.Recognizer()

def SpeakText(command):
    engine = pyt.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    r1.adjust_for_ambient_noise(source2, duration=2)

    print("Listening...")
    audioInput = r1.listen(source2)

    speechText = r1.recognize_google(audioInput)
    speechText = speechText.lower()

    print("You said " + speechText)