import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pyt

# Recognizer
r1 = sr.Recognizer()

# Text to speech
def SpeakText(command):

    # Initialize engine
    engine = pyt.init()
    engine.say(command)
    engine.runAndWait()


with sr.Microphone() as source2:

    # Calibrating ambient noise
    print("Calibrating npise threshold")
    r1.adjust_for_ambient_noise(source2, duration=2)

    print("Listening...")
    audioInput = r1.listen(source2)

    speechText = r1.recognize_google(audioInput)
    speechText = speechText.lower() # Text to speech converter 

    print("You said: " + speechText)