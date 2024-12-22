# Voice Assistance Project Documentation

## Overview
This project implements a basic voice assistant in Python. The assistant uses voice commands to perform various tasks like opening websites, telling jokes, and playing songs. It incorporates modules for speech recognition, text-to-speech synthesis, and system interaction.

---

## Features
1. *Voice Command Recognition:*
   - Recognizes user commands using speech recognition.

2. *Text-to-Speech Output:*
   - Responds to commands with synthesized speech.

3. *Functionalities:*
   - Greets the user.
   - Responds to queries about its name and age.
   - Tells the current time.
   - Opens YouTube or a web browser.
   - Tells a joke.
   - Plays a predefined song.
   - Shuts down on command.

---

## Requirements
Below is a list of Python modules required for this project:

```plaintext
comtypes==1.4.8
PyAudio==0.2.14
pyjokes==0.8.3
pypiwin32==223
pyttsx3==2.98
pywin32==308
SpeechRecognition==3.12.0
typing_extensions==4.12.2
```


To install the dependencies, run the following command:
bash
pip install -r requirements.txt


---

## Code Explanation

### *Importing Modules*
```python
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
```

- `pyttsx3`: Text-to-speech conversion library.
- `speech_recognition`: Library for recognizing speech.
- `webbrowser`: Allows interaction with web browsers.
- `datetime`: Fetches current date and time.
- `pyjokes`: Generates jokes.
- `os`: Provides interaction with the operating system.

### *Speech Recognition Function*
```python
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
```
- Captures audio input from the user via the microphone.
- Converts the audio to text using Google’s speech recognition API.
- Returns the recognized text or an error message.

### *Text-to-Speech Function*
```python
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()
```
- Uses `pyttsx3` to `synthesize` speech.
- Configures voice and speech rate.

### *Main Functionality*
```python
if __name__ == "__main__":
    if sptext().lower() == "hello jarvis":
        speechtx("Hello sir, how can i help you")
        while True:
            data1 = sptext().lower()
            # Handling specific commands...
```
- Waits for the user to say “Hello Jarvis” to initiate the assistant.
- Responds to various commands within a loop:
  - *Name Query:* Replies with its name.
  - *Mood Query:* Replies with its mood condition.
  - *Age Query:* Responds humorously to age-related questions.
  - *Time Query:* Tells the current time.
  - *YouTube:* Opens YouTube in the web browser.
  - *Browser:* Opens a generic browser window.
  - *Joke:* Tells a random joke using pyjokes.
  - *Play Song:* Plays a predefined song from a specified directory.
  - *Shutdown:* Exits the assistant.

### *Example Commands*
- *Trigger:*
  
  Hello Jarvis
  
- *Commands:*
  ```plaintext
  What is your name?
  How are you?
  How old are you?
  What is the time now?
  Open YouTube
  Open browser
  Tell me a joke
  Play song
  Shut down
  ```

---

## Directory Structure
```plaintext
VoiceAssistant/
|— main.py  # Main Python script
|— requirements.txt  # Dependencies
|— music/  # Directory containing songs
```

---

## Usage
1. Ensure all dependencies are installed using the requirements.txt file.
2. Update the song directory path in the play song section.
3. Run the script:
   bash
   python main.py
   
4. Interact with the assistant using voice commands.

---

## Notes
- Ensure your microphone is properly configured and accessible.
- If the assistant doesn’t recognize speech accurately, adjust for ambient noise and retry.

---

## Potential Enhancements
1. *Dynamic Command Addition:* Allow users to add new commands.
2. *Error Handling:* Improve recognition accuracy and error feedback.
3. *Integration:* Expand functionalities, such as sending emails or setting alarms.
4. *GUI:* Add a graphical interface for better interaction.

---

## License
This project is open-source and available under the MIT License.