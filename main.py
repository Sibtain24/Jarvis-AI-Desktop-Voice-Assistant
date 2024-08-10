# Mega-Project: Creating a desktop voice assistant (Jarvis)

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import google.generativeai as genai
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text): # Function to transcribe speech to text
    engine.say(text)
    engine.runAndWait()

def processCommand(c): # Function to process different commands given by the user

    # Command to search a query in google (Google Search):

    if "search in google for" in c.lower(): # Say - "search" to search something in google.com
        l = c.lower().split(" ")[4: ]
        query_google = " ".join(l)
        speak(f"Searching in google for {query_google}")
        webbrowser.open(f"https://www.google.com/search?q={query_google}")

    # Creating Command to search a query in youtube (YouTube Search):

    elif "search in youtube for" in c.lower(): # Say - "YouTube Search" to search something in google.com
        l = c.lower().split(" ")[4: ]
        query_yt = " ".join(l)
        speak(f"Searching in YouTube for {query_yt}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query_yt}")
    
    # Creating Commands for Opening Websites in default browser:

    elif "open google" in c.lower(): # Say - "open google" to open google.com in browser
        speak("Opening google.com in your default browser")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower(): # Say - "open youtube" to open youtube.com in browser
        speak("Opening youtube.com in your default browser")
        webbrowser.open("https://www.youtube.com")
    
    elif "open gmail" in c.lower(): # Say - "open gmail" to open mail.google.com in browser
        speak("Opening gmail in your default browser")
        webbrowser.open("https://mail.google.com/mail/u/0/")
        
    elif "open github" in c.lower(): # Say - "open github" to open github.com in browser
        speak("Opening github.com in your default browser")
        webbrowser.open("https://github.com/")

    elif "open my github profile" in c.lower(): # Say - "open google" to open google.com in browser
        speak("Opening your github profile in your default browser")
        webbrowser.open("https://github.com/Sibtain24/")

    # Creating Commands for opening desktop Apps:

    elif "open microsoft edge" in c.lower() or "open edge" in c.lower(): # Say - "open edge"
        speak("Opening Microsoft Edge...")
        app_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
        os.startfile(app_path)

    elif "open chrome" in c.lower(): # Say - "open chrome"
        speak("Opening Google Chrome...")
        app_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
        os.startfile(app_path)

    elif "open word" in c.lower() or "open microsoft word" in c.lower(): # Say - "open Word"
        speak("Opening Microsoft Word...")
        app_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
        os.startfile(app_path)

    elif "open excel" in c.lower() or "open microsoft excel" in c.lower(): # Say - "open Excel"
        speak("Opening Microsoft Excel...")
        app_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
        os.startfile(app_path)

    elif "open powerpoint" in c.lower() or "open microsoft powerpoint" in c.lower(): # Say - "open PowerPoint"
        speak("Opening Microsoft PowerPoint...")
        app_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
        os.startfile(app_path)

    elif "open notepad" in c.lower(): # Say - "open notepad"
        speak("Opening Notepad..")
        app_path = r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2405.13.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe"
        os.startfile(app_path)

    elif "open calculator" in c.lower(): # Say - "open calculator"
        speak("Opening Calculator...")
        app_path = r"C:\WINDOWS\system32\calc.exe"
        os.startfile(app_path)
    
    # Creating command for writing emails, letters, essays or speech using Gemini AI in AI_Response.txt file:
    
    elif c.lower().startswith("write"): # Start a command with the word - "Write"
        output = aiProcess(c)
        with open("AI_Response.txt", "w") as mail:
            mail.write(output)
        speak("Done writing! Check the AI Response.text file")

    # Creating Command to play your favorite music or playlist from musicLibrary.py file:

    elif c.lower().startswith("play"): # Say the word "play" followed by the "name" of the music saved in musicLibrary.py file's dictionary
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        speak("Playing now...")
        webbrowser.open(link)

    # Creating Command to stop Jarvis/Program:

    elif c.lower()=="deactivate" or c.lower()=="stop": # Say "deactivate" or "stop" to exit the Program
        print("Deactivating Jarvis...")
        speak("Deactivating Jarvis...")
        exit()
    
    else:
        # Let Gemini AI handle the request
        output = aiProcess(c)
        speak(output)

# Function to connect GeminiAI API to python and process the queries to fetch responses:

def aiProcess(command):

    genai.configure(api_key="YOUR_API_KEY")

    command = f"Please be precise and concise, and avoid unnecessary punctuation. Respond as if you are having a conversation but don't ask questions at the end. Also, when you are told to write something, respond in detail. {command}"

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 5000,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(command)

    return response.text

if __name__ == "__main__":
    
    speak("Initializing Jarvis...")

    while True:

        # Listen for the wake word 'Jarvis'
        # obtain audio from the microphone:
        r = sr.Recognizer()
        
        # recognize speech using Google:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("Yes! How may I help you?")
                # Listen for command:
                with sr.Microphone() as source:
                    print("Jarvis is Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error! Try speaking again; {0}".format(e))
