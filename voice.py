import sys
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyaudio
import pyjokes
import requests
from bs4 import BeautifulSoup
import html
import Calculator
#import calculator_py
name="sir"

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

#change voice Rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("hello world")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {name}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {name}")
    else:
        speak(f"Good Evening {name}")
    speak(" i am your voice assistent. please tell how can i help you")


def take_command():

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
        # print(e)
        speak("say that again please")
        print("Say that again please...")
        return "None"
    return query



def run_voice():
    while True:
        command = take_command().lower()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            speak("playing" + song)
            pywhatkit.playonyt(song)
        elif 'hello' in command:
            speak(f"hello{name},how are you")
        elif 'am fine' in command:
            speak(f"that's great {name}")
        elif'thank you' in command:
            speak(f"welcome {name}")

        elif 'open chrome' in command:
            path = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            os.startfile(path)
        elif 'open google' in command:
            webbrowser.open("google.com")
        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'check notification on facebook' in command:
            webbrowser.open("facebook.com")
            speak("okay, checking facebook notification")
        elif 'time' in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print(time)
            speak(time)

        elif "temperature" in command:
            search = "temperature in sri lanka"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
        #elif ' score' in command:
         #   search1=command().lower()
          #  url1=f"https://www.google.com/search?q=ipl+score&oq={search1}"
          #  re=requests.get(url1)
           # data1=BeautifulSoup(r.text,"html.parser")
           # score=data1.find("div", class_="BNeawe").text
            #speak(f"current{search1}is {score}")
        elif 'ipl score' in command:
            webbrowser.open("https://www.google.com/search?q=ipl+score&sxsrf=APwXEdeYDngKgJ6lP5g3DL6KFATD2cxjHg%3A1684579400306&source=hp&ei=SKRoZKH9ENqSoATQqo3wBQ&iflsig=AOEireoAAAAAZGiyWFuCd9aKzx0sQdQ5UfNADHtfzJCN&ved=0ahUKEwihwf-l24P_AhVaCYgKHVBVA14Q4dUDCAk&uact=5&oq=ipl+score&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjEIoFECcQRhD9ATINCAAQigUQsQMQgwEQQzINCAAQigUQsQMQgwEQQzINCAAQigUQsQMQgwEQQzINCAAQigUQsQMQgwEQQzINCAAQigUQsQMQgwEQQzINCAAQigUQsQMQgwEQQzIHCAAQigUQQzINCAAQigUQsQMQgwEQQzIHCAAQigUQQzoHCCMQ6gIQJzoHCCMQigUQJzoNCC4QigUQsQMQgwEQQzoLCAAQgAQQsQMQgwFQyQNY8xlg2htoAXAAeACAAfoBiAHgDZIBBTAuMS43mAEAoAEBsAEK&sclient=gws-wiz")
        elif 'who is ' in command:
            import wikipedia as googlescrap
            command = command.replace('who is', '')
            command = command.replace('google', '')
            speak("this is what i found on the web!")
            try:
                pywhatkit.search(command)
                results = googlescrap.summary(command, sentences=3)
                print(results)
                speak(results)
            except:
                speak("nothing found")
        elif 'music' in command:
            music_dir = 'C:\\Users\\kugesh\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'shutsown pc ' in command:
            speak("okay")
            sec = 7
            os.system((f"shutdown /s /t {sec}"))
            speak(f"bye {name} have a good day")
            speak(f"am going to shutdown pc within{sec}second")
            sys.exit()

        elif 'stop listen' in command:
            print(f"okay{name} i stop listening")
            speak(f"okay{name} i stop listening")
            break
        elif 'wikipedai' in command:
            speak("searching on wikipedai")
            command=command.replace('wikipedai','')
            results1=wikipedia.summary(command,sentences=3)
            speak("according to wikipedia")
            print(results1)
            speak(results1)
        elif 'exit' in command:
            exit()
        elif 'show my friends pic' in command:
            webbrowser.open("https://drive.google.com/drive/folders/1ZiauBR3PBRo7q_2FQnp_2E_RIxfwktDV?usp=share_link")
        elif 'name of the ex girlfriend ' in command:
            speak("ex name is OE")
        elif "open family folder on my google drive" in command:
            webbrowser.open("https://drive.google.com/drive/folders/17vaSLoImxcDuYGrJdSpjEZV3zB4L6G-2?usp=share_link")
        elif 'reason for my sadness' in command:
            speak("here this is reason for your sadness")
            webbrowser.open("https://drive.google.com/file/d/1bEhHFV5kHTRJr7jpoScTk90yh5OY9VL5/view?usp=share_link")
        elif 'my favourite thought' in command:
            print("love is illusion fucking is truth!")
            speak("Love is illusion fucking is truth")
        elif 'my favourite song' in command:
            speak("here this is your favourite song")
            webbrowser.open("https://www.youtube.com/watch?v=1Yg6R2KOkZg")
        elif 'my favourite breakup song' in command:
            speak("here this is your favourite breakeup song")
            webbrowser.open("https://www.youtube.com/watch?v=X0ss4GI0RCA&pp=ygUWaW1haWtrYWEgbm9kaWdhbCBzb25ncw%3D%3D")
        elif 'song for ' in command:
            webbrowser.open("https://www.youtube.com/watch?v=hPzf3CnjapU")
        elif 'open code on github' in command:
            webbrowser.open("")
        
        
        
        
        #elif "ipl score" in command:
         #   from player import notification  # pip install plyer
          #  import requests  # pip install requests
          #  from bs4 import BeautifulSoup  # pip install bs4
          #  url = "https://www.cricbuzz.com/"
          #  page = requests.get(url)
          #  soup = BeautifulSoup(page.text, "html.parser")
          #  team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
           # team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
          #  team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
          #  team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

           # a = print(f"{team1} : {team1_score}")
            #b = print(f"{team2} : {team2_score}")

           # notification.notify(
           #     title="IPL SCORE :- ",
            #    message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
             #   timeout=15
        #    )
        #elif 'email' in command:
         #   try:
          #      speak("what should i say?")
           # content=take_command()
            #to="kugeshkuge1278@gmail.com"
            #sendemail

        elif 'open whatsapp' in command:
            webbrowser.open("whatsapp.com")
        #elif 'send message' in command:
         #   msg=pywhatkit.sendwhatmsg('+94743445210','hi am kugesh',time)
       # elif "calculate" in query:
        #    from calculator_py import WolfRamAlpha
         #   from calculator_py import Calc
          #  query = query.replace("calculate", "")
           # Calc(query)






#wishMe()
#run_voice()
if __name__ == '__main__':
    wishMe()
    run_voice()

