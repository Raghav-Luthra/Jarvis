import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:
            print(e)
            speak("say that again please")
            return"None"
        return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching the wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak ("Accourding to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'C:\\music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs [0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")
            print(strTime)

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\ragha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'open chrome' in query:
            bravePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravePath)

        elif 'open link' in query:
            webbrowser.open("linkedin.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open gmail' in query:
            webbrowser.open("main.google.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open pinterest' in query:
            webbrowser.open("pinterest.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open classroom' in query:
            webbrowser.open("edu.google.com/workspace-for-education/classroom/")

        elif 'open discord' in query:
            webbrowser.open("discord.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open ebay' in query:
            webbrowser.open("ebay.com")

        elif 'open documents' in query:
            webbrowser.open("docs.google.com")

        elif 'open drive' in query:
            webbrowser.open("drive.google.com")

        elif 'open photos' in query:
            webbrowser.open("photos.google.com")

        elif 'open translater' in query:
            webbrowser.open("translate.google.com")

        elif 'open news' in query:
            webbrowser.open("news.google.com")

        elif 'open chess' in query:
            webbrowser.open("chess.com")

        elif 'open codetantra' in query:
            webbrowser.open("srmist.codetantra.com")

        elif 'quicklearn' in query:
            webbrowser.open("quicklrn.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open anime' in query:
            webbrowser.open("zoro.to")

        elif 'open spotify 'in query:
            webbrowser.open("open.spotify.com")

        elif 'play' in query:
            query = query.replace('play','')
            speak(query)
            pywhatkit.playonyt(query)

        elif 'search on google' in query:
            query = query.replace('search on google','')
            speak(query)
            pywhatkit.search(query)
        
        elif 'what is' in query:
            app_id = ''
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak(answer)




