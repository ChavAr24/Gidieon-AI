# Gidieon.py is a small AI like the "Jarvis" in the movie "Iron Man" and its sequels.
# This program can do small works like open a music track and play it, open any websites like youtube or stackoverflow.
# At the moment I haven't made it do a lot of things but the limits are endless for this AI.
# By: Aryan chavan

# Modules needed for the AI (The comments after the module names are how you can download them using PIP)
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui # pip install pyautogui (for pressing the keys Example: ctrl,shift,letters,number,punctuationand etc)


def hit(key):       # definning the key pressing function
    pyautogui.press(key, presses=2)
    return

# the code for the AI to speak
# there are 2 voices already installed when you install the pyttsx3 module.
# you can Download more voices.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)   # At the moment the voice is set to the female voice
# 0 is for the already installed male voice and 1 is for the already installed female voice


def speak(audio):   # A function that lets the AI speak.
    engine.say(audio)
    engine.runAndWait()


def wishMe():   # A function that wishes you according to time when you run the code.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi..Sir!")       

def takeCommand():  #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...") 
        speak("Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):     # A function to send emails using the SMTP lib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")   

        elif 'stop running the code' in query:
            speak("Stopping the code Run")            
            print("Stopping the code Run")
            pyautogui.hotkey('ctrl', 'alt', 'm')
        
        elif 'increase the volume' in query:
            speak("Increasing the volume")            
            print("Increasing the volume")
            hit("volumeup")

        elif 'decrease the volume' in query:
            speak("Decreasing the volume")            
            print("Decreasing the volume")
            hit("volumedown")
          
        elif 'who am i' in query:
            speak("It depends on who is asking")
            print("It depends on who is asking")

        elif 'play music' in query:
            music_dir = '#the path of the file or folder'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "#the path of the file or folder"
            os.startfile(codePath)

        elif 'open Maya' in query:
            mayaPath = "#the path of the file or folder"
            os.startfile(mayaPath)


        # note: I haven't had any success to get the email function to work..
        elif 'send email to "The person you want to send email to"' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "---"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am sorry sir... the mail could not be sent.")    

#  There are some parts of this code that need a bit of work..
#  I have made this code asper how it suits me but you can change the code to how it suits you and changing things it can do
