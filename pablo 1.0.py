import pyttsx3 
import datetime
import speech_recognition as sr
from twilio.rest.api.v2010 import account
import wikipedia
import webbrowser as wb
import pyjokes
from twilio.rest import Client



engine = pyttsx3.init()




def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def time_():
    #horario de 12 hrs
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Bro")
    time_()
    date_()
    
    #Greetings
    
    hour = datetime.datetime.now().hour
    
    if hour>= 6 and hour<12:
        speak("Good Morning Bro")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon Bro")
    elif hour >=18 and hour<24:
        speak("Good Evening Bro")
    else:
        speak("Good Night Bro")
    
    speak("How can I help you today?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            #query = r.recognize_google(audio, language='en-US')
            query = r.recognize_google(audio)
            print(query)
        #    print("Did you say "+ r.recognize_google(audio))
        except Exception as e:
            print(e)
            speak("Can you repeat that please")
            return "None"
        return query
       #     print("Can you repeat that please")       
       

def joke():
    speak(pyjokes.get_joke())

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
    #enable low security in gmail 
    
    server.login("", "")
    server.sendmail('',to, content)
    server.close()


  

#print(message.sid)
    
    
    
    
if __name__ == '__main__':
    
    
    wishme()
    
    while True:
        query = TakeCommand().lower()
        #Everything to lwr case 
        
        
        #ifs for the commds
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            
            speak("Searching")
            #replacing the query with blank
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query,sentences=2)
            speak('Wikipedia says')
            
            #print and speak the result
            print(result)
            speak(result)
        
        elif 'open chrome' in query:
            speak("What should I search?")
            #the chromepath
            chromepath ="/opt/google/chrome/chrome %s"
            
            search = TakeCommand().lower()
            #only wbs that in .com
            wb.get(chromepath).open_new_tab(search+'.com')
        

        elif 'text' in query:
            speak("What should I say?")

            message = TakeCommand().lower()
            speak(f'is {message} correct?')

            confirm = TakeCommand().lower()

            if(confirm in 'yes' or 'correct'):
                account_sid = ''
                auth_token = ''
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                from_='',
                 body=message,
                 to='')
                 speak('I have finished')
            
            else:
                speak('Please repeat the message')
        
        
            
            

        
        elif 'search youtube' in query:
            speak("What should I search?")
            search_term = TakeCommand().lower()
            speak("Okay I will do that")

            wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif 'search google' in query:
            speak("What should I search?")
            search_term = TakeCommand().lower()
            speak("Please wait")
            wb.open('https://www.google.com/search?q='+search_term)
        
        elif 'joke' in query:
            joke()
        
        elif 'power off' in query:
            speak('Later bro')
            quit()

        elif 'take note' in query:
            speak("What should I write bro?")
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            speak('Should I include the date?')
            answer = TakeCommand().lower()

            if 'yes' in  answer or 'okay' in answer:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                speak("I have finished")

            else :
                file.write(notes)


        '''
        
        elif 'send email' in query:
            try:
                speak("What should I say")
                content = TakeCommand()
                speak("Who is the receiver")
                receiver = input("Enter Receiver's Email: ")
                
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak('Email has been sent..')
            
            except Exception as e:
                print(e)
                speak("Unable to send Email")
        '''        
                    

    
    
