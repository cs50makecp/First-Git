import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import googlesearch
listener=sr.Recognizer()
alexa=pyttsx3.init()
voices=alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_commend():
    try:
       with sr.Microphone() as source:
           print("listening........")
           voice= listener.listen(source)
           command= listener.recognize_google(voice)
           command=command.lower()
           if 'alexa' in command:
                command=command.replace('alexa','')


    except:
        pass
    return command

def run_alexa():
    command=take_commend()
    if 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is:'+time)
    elif 'play' in command:
        song=command.replace("play",'')
        talk("playing"+song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        lookfor=command.replace('tell me about','')
        info=wikipedia.summary(lookfor,5)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'relation' in command:
        talk("Sorry vaiya,I am already in a relationship.so there is no question of having a relationship with you")

    elif "who is your creator" in command:
        talk("my creator name is mohammad Raihan  Hossen. he is student")
    elif 'search about' in command:
        sea=command.replace("search about","")
        search=webbrowser.Chrome(googlesearch.search(sea))
        print(search)
        talk(search)

    elif 'call now' in command:
        call=command.replace('call now','')
        talk("I am calling")
        number="+8801409370489"
        phone="+8801400631882"
        with sr.Microphone() as source:
            print("withimng a magfb........")
            voice = listener.listen(source)
            ma = listener.recognize_google(voice)
            ma =ma.lower()
            if 'alexa' in ma:
                ma = ma.replace('alexa', '')

        masge=ma
        if 'number' in call:
            pywhatkit.sendwhatmsg_instantly(number,masge,30,10)
            return take_commend()
        elif 'phone' in call:
            pywhatkit.sendwhatmsg_instantly(phone,masge,30,10)
            return run_alexa()


    else:
        talk('sorry I can hear you')
        pywhatkit.search(command)

#talk("How one the help")
while True:
    run_alexa()

