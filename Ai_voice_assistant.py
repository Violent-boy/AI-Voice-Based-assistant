from binascii import b2a_hex
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! ")

    else:
        speak("Good Evening! ")

    speak (f" Hello {name}  how may i help you")    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("not matched with open please say that again")
        return "None"
    return query    

if __name__ == "__main__":
    os.system("cls")
    print('\t\t WElCOME TO YOUR VOICE ASSISTANT')
    print("\t\t==================================")
    speak("Welcome to your voice assitant")
    print("Enter your name : ")
    speak("Enter your name ")
    name =input()
    print("Enter your age ")
    speak(f"Thankyou {name} Enter your age also ")
    age = int(input())
    wishMe(name)
    os.system("cls")
    print('\t\t WElCOME TO YOUR VOICE ASSISTANT')
    print("\t\t==================================")
    print("\tLet me help you ")
    print("\t----------------")
    speak("let me help you ") 
    print("To Search in Wikipdia --> say according to wikipedia in the last ")
    speak("To Search in Wikipdia say according to wikipedia in the last ")
    print("To open the youtube --> say open youtube")
    speak("To open the youtube say open youtube")
    print("To open the google --> say open google")
    speak("To open the google say open google")
    print("To open the Amizone --> say open Amazone")
    speak("To open the amizone say open amazone")
    print("To open the Whatsapp web --> say open whatsapp")
    speak("To open the whatsapp web say whatsapp")
    print("To open the G-mail --> say open G-mail")
    speak("To open the gmail say open gmail") 
    print("To check the present time --> say the time ")   
    speak("To check the present time say the time ")
    print("to check you are elgible for vote or not --> say age")
    speak("to check you are elgible for vote or not say age")
    print("For exit the program ---> say exit")
    speak("For exit the program say exit ")
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query  = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'open amazon' in query:
        webbrowser.open('amazon.in')
    elif 'open whatsapp' in query:
        webbrowser.open('web.whatsapp.com')
    elif 'open gmail' in query:
        webbrowser.open('mail.google.com') 
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f"{name} , the time is {strTime}")   
    elif 'age' in query:
        if age < 18:
            speak(f"sorry {name} you are not eligible for vote")
        elif age == 18:
            speak(f" {name} wait one year as well for perfect eligibilty ")
        else:
            speak(f"congrats {name} you are eligible " )
    elif "exit" in query:
        os.system("cls")
        print("\t\n\tThankyou for visit !! Have a nice day ")
        print("\t==========================================")
        speak("Thankyou for visit Have a nice day ")
        break
    else : 
        speak("say only the abvoe list")
            
                              