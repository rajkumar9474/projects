import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not understanding ")
            return "not understanding"

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":
    if sptext().lower() == "hello jarvis":
        speechtx("Hello sir, how can i help you")
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                var = "my name is jarvis"
                speechtx(var)
            elif "how are you" in data1 or "how r u" in data1:
                var = "i am fine, thank you, hope you are also fine"
                speechtx(var)
            elif "old are you" in data1:
                var = "why do you want to know my age? i will not tell you"
                speechtx(var)
            elif "time now" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(f"the time is {time} approximately")
            elif "youtube" in data1:
                speechtx("opening youtube")
                webbrowser.open("https://www.youtube.com")
            elif "browser" in data1:
                speechtx("opening brave browser")
                webbrowser.open("https://www.google.com")
            elif "joke" in data1:
                joke = pyjokes.get_joke(language="en",category="all")
                print(joke)
                speechtx(joke)
            elif 'play song' in data1:
                add = "music"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[1]))
            elif 'shut down' in data1:
                speechtx("goodbye sir, have a nice day")
                break
            elif 'shutdown' in data1:
                speechtx("goodbye sir, have a nice day")
                break
    else:
        print("thanks")
    
