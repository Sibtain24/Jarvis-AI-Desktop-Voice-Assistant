# Project: AI Desktop Voice Assistant (Jarvis)

![JARVIS-AI Desktop Voice Assistant](https://github.com/user-attachments/assets/a88429ef-b4bb-4407-abd8-325f0e11e024)

This is an AI powered Virtual Desktop Assistant named "Jarvis" created in Python. When you run this program, you can ask the program to do various tasks. Currently, this program is capable of performing the following tasks:
1) AI Response using Google's Gemini AI.
2) Searching for a query on Google.
3) Searching for a video on YouTube.
4) Writing Email, Letter, Speech, Essay etc using Gemini AI.
5) Opening a few Websites like Google, YouTube, GMail and GitHub in default browser.
6) Opening a few apps like Microsoft Edge, Google Chrome, Word, Excel, PowerPoint, Visual Studio Code, Command Prompt, Notepad and Calculator.
7) Playing Online Music or Playlist (saved in the 'musicLibrary.py' file).

## Instructions to Run Jarvis:

1) Download the Source File as zip by clicking on the 'Code' button on this web page and selecting 'Download as ZIP'.

2) Extract and open the folder in VS Code.

3) Make sure you have Python installed in your PC and connect it to Visual Studio Code (If you don't know how to do this, you can watch a tutorial on YouTube to setup Visual Studio Code for Python development).

4) Open your terminal application and install the following modules / packages before running the program:<br>
    a) Speech recognition : `pip install SpeechRecognition`<br>
    b) Pyttsx3 : `pip install pyttsx3`<br>
    c) Google Generative AI : `pip install google-generativeai`<br>
    d) PyAudio : `pip install PyAudio`<br>
    You can copy and paste the pip commands from the above to save some time.

6) Now, you need to go to the Gemini API website and create an API key for yourself. To create an API key, [Click Here](https://ai.google.dev/gemini-api/docs/api-key). After creating an API key, Copy and Paste the key in place of "YOUR_API_KEY" written under _aiProcess_ function in the 'main.py' file.<br>[Note: You can also use OpenAI API for which you will need to pay some money. To use OpenAI API, you need to replace the code under "aiProcess" function with the code written in 'api_openai.py' file. You can do that by simply copying the code and pasting it under "aiProcess" function. Also, you will need to install OpenAI Package, for that, copy and paste this: `pip install openai` ]

5) Run 'main.py' file.

6) Jarvis will start by saying, _"Initializing Jarvis..."_. 

7) Then it will listen for you to say "Jarvis" to activate the operation. You will need to say _"Jarvis"_ everytime you want to perform a task. 
For example, when you say **_"Jarvis"_**, then it will respond by saying _"Yes! How may I help you._" and after that you will need to ask any question that you want an answer to and the Gemini AI will respond to you or you will need to say the pre-defined commands to do certain tasks that are mentioned below.

8) There are some pre-defined commands to do specific tasks. These are as follows:

    a) You can ask any question to **Gemini AI** by directly speaking out the question and you will get a response. (NOTE: Gemini AI tends to give long answers to if you want to have brief answers the you can tell it to keep the response short and concise.)<br>
        _For example: You asked, ***"What is Python Programming Language? Give me a short and concise answer"***. As soon as you ask a question, you will get the answer from Gemini AI_.
    
    b) For performing google searches, you need to say ***"Search in Google for"*** followed by your query that you want the results for.<br>
        _For example: When you will say, ***"Search in Google for Free Python Programming Courses"***, it will search for "Free Python Programming Courses in google.com in your default browser._
     [Note: You will need to say "Search in Google for" to search anything in google otherwise it won't work.]
     
    c) For performing YouTube searches, you need to say ***"Search in YouTube for"*** followed by your query that you want the results for.<br>
        _For example: When you will say, ***"Search in YouTube for Python Programming Tutorial"***, it will search for "Python Programming Tutorial" videos in youtube.com in your default browser._
     [NOTE: You will need to say "Search in YouTube for" to search for youtube videos otherwise it won't work.]
    
    d) For **opening websites** you have to say _"open"_ followed by the name of websites like Google, YouTube, GitHub. You can add more of your favorite websites by adding the names and links in program's code (in main.py file).<br>
        _For example: When you will say, ***"open google"***, then it will open google.com in your default browser. Likewise, you can say the names of other websites after saying "open"_. 
     [NOTE: You can only open Google, YouTube, GMail and GitHub by default, but you add can add some more commands and websites manually by adding the codes.]
    
    e) For **opening apps** in your PC, you have to say _"open"_ followed by the name of apps like Chrome, Microsoft Edge, Word, Excel, PowerPoint, Visual Studio Code, Command Prompt, Notepad and Calculator.<br>
        _For example: When you will say, ***"open VS Code"*** or ***"open Visual Studio Code"***, it will open Visual Studio Code App in your PC. Likewise, you can say the names of other apps mentioned above to open them._

    f) For **writing emails, letters, essays etc**, you need to start the command by saying the word _"write"_ followed by what you want to write.<br>
        _For example: If you said, ***"Write a formal email to my boss. I work in [this company] and the subject of the email is regarding [subject]."***, then Gemini AI will write the email in 'AI_Response.txt' file, which will be automatically created if not already present in the Jarvis Project folder._
   
    g) For **playing music** online, you need to say, "_open_" followed by the name of the song.<br>
        _For example: When you will say, ***"play wanted"*** it will play the song called "Wanted" in your browser. To add custom songs or playlist, open the 'musicLibrary.py' file and then replace the dictionary key with the name of your favourite music and replace the value with the link of your favorite song or playlist._
    
    h) Lastly, to **quit** or **deactivate** Jarvis, you have to say ***"deactivate"*** or ***"stop"***, and the program will stop running. To run the program again, you will need the 'main.py' file again is Visual Studio Code.

***I will keep on imroving this program over time and will give it, its own GUI and will add more functionality***🎯
