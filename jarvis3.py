import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import subprocess
import platform

# Speech recognition
def sp():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening now...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service: {e}")
        return None

# Text-to-speech
def speech(text):
    if text:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Use female voice
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
    else:
        print("Nothing to speak.")

# Cross-platform file opener
def open_file_cross_platform(file_path):
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(file_path)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", file_path])
        else:  # Linux or others
            subprocess.Popen(["xdg-open", file_path])
    except Exception as e:
        print("Error opening file:", e)
        speech("Sorry, I could not open the file.")

# Initial trigger
x = sp()
print("Recognized:", x)
speech(x)

# Main loop
if __name__ == "__main__":
    if x and "hey peter" in x.lower():
        while True:
            data1 = sp()
            if data1:
                data1 = data1.lower()

                if "your name" in data1:
                    speech("My name is Peter")

                elif "old are you" in data1:
                    speech("I am one year old")

                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    speech(f"The time is {time}")

                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif "joke" in data1:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    speech(joke)

                elif "play song" in data1:
                    folder_path = r"D:\song"  # Replace with a real folder on your machine
                    try:
                        songs = os.listdir(folder_path)
                        if songs:
                            first_song_path = os.path.join(folder_path, songs[0])
                            print("Playing:", first_song_path)
                            open_file_cross_platform(first_song_path)
                        else:
                            speech("No songs found in the folder.")
                    except Exception as e:
                        print("Error:", e)
                        speech("I couldn't play the song. Please check the folder.")

                elif "exit" in data1:
                    speech("Thank you. Goodbye!")
                    break
                else:
                    speech("Sorry, I didn't catch that.")
            else:
                speech("I didn't hear anything.")
    else:
        print("Trigger phrase not detected. Exiting...")
