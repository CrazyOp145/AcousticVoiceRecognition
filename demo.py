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
    print("Calibrating noise threshold")
    r1.adjust_for_ambient_noise(source2, duration=2)

    print("Listening...")
    audioInput = r1.listen(source2)
    
    # Exception handling
    try:
        speechText = r1.recognize_google(audioInput)
        print("You said: " + speechText)

        SpeakText('Got your message')

    except Exception as e:
        print("Error: " + str(e))


