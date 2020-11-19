import speech_recognition as sr
import pyttsx3 as pt #librairie pour convertir le speech en text  // Supports multiple TTS engines, including Sapi5, nsss, and espeak.
import wikipedia  # librairie pour acceder à des informations disponibles sur wikipedia
import webbrowser # permet d'afficher des documents sur le Web
import time  # librairie pour gérer les tâches liées au temps
import datetime # librairie pour munipler la date et l'heure


engine=pt.init('sapi5')  #Sapi5 Microsoft Speech API - permettre l'utilisation de la reconnaissance vocale et de la synthèse vocale dans les applications Windows




#assistant_speaking : convertit le texte en parole. La fonction prend un text comme argument, puis initialise l'engine
def assistant_speaking(speech):
    engine.say(speech)  #l'assistant prononce le speech en parametre 
    engine.runAndWait()  #pour bloquer, toutes les commandes actuellement en file d'attente pendant le traitement.



#hello : pour dire hello à l'utilisateur de plusieurs manières 
def hello():
    hour=datetime.datetime.now().hour  #donne le temps actuelle
    # on va traiter 4 cas pour dire Hello tout depend de l'heure actuelle
    if hour>=4 and hour<12:
        print("Hello,Good Morning")
        assistant_speaking("Hello,Good Morning,Have a nice day friend")
        
    elif hour>=12 and hour<18:
        print("Hello,Good Afternoon")
        assistant_speaking("Hello,Good Afternoon")
        
    elif hour>=18 and hour<23:
        print("Hello,Good Evening, you still have a long night to do many things, stay positive!")
        assistant_speaking("Hello,Good Evening, you still have a long night to do many things, stay positive!")
        
    else:
        print("Hi,its never too late to work, have a good night!")
        assistant_speaking("Hi,its never too late to work, have a good night!")
        
		
		
#assistant_recognize_voice  : permet d'entendre la voix de l'utilisateur à l'aide de microphone et reconnaitre se qu'il a dit 
def assistant_recognize_voice():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:  # on a le microphone comme un source d'entrée 
        print("Listening...")
        vocal=recognizer.listen(source) # pour enregister la voix de l'utilisateur

        try:   
            statement=recognizer.recognize_google(vocal,language='en-in')  # on utilise google audio recognizer pour reconnaître la parole.
            print(f"user said:{statement}\n")

        except Exception as e:   #gérer les exceptions qui peuvent intervenir ; par exemple l'assistant ne vous entend pas bien à cause de microphone par exemple.
            assistant_speaking("i cant hear you very well, I think you should repeat what you said.")
            return "None"
        return statement




if __name__=='__main__':

    hello() # premier chose à faire c'est de dire Hello à l'utilisateur tout depend de l'heure actuelle
    while True: # cette boucle est infini jusqu'à terminer le parole avec le bot en disant GoodBye 
        
        assistant_speaking("how can I help you now?")  # il va demander aprés chaque tache si l'utilisateur aura besoin d'autres demandes.
        statement = assistant_recognize_voice().lower()  # retourner le parole de l'utilisateur  
        
        if statement==0: #on fait rien s'il est vide
            continue
            
        if "goodbye" in statement or "ok bye" in statement or "stop" in statement:  # si le parole contient l'un de ces mots alors il va s'arreter automatique et dire goodbye
            print('Ok good bye see you later')
            assistant_speaking('Ok good bye see you later')
            break
            
        elif 'time' in statement: # si l'utilisateur a demandé de connaitre l'heure actuelle
            actualTime=datetime.datetime.now().strftime("%H:%M:%S") # strftime pour convertir datetime en String 
            assistant_speaking(f"the time is {actualTime}")
            
        elif 'search'  in statement: # si l'utilisateur a demandé de lancer une recherche sur le web 
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(4)  
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement or "who invented you" in statement: # si l'utilisateur a demandé de savoir l'inventeur de ce Bot
            assistant_speaking("I was built by maryem samet")
            print("I was built by maryem samet")
        elif'wikipedia' in statement: # si l'utilisateur a demandé de faire une recherche sur wikipedia
            assistant_speaking('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            assistant_speaking("According to Wikipedia")
            print(results)
            assistant_speaking(results)
