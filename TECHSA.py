#MADE BY DAYAL PRATHAP


from __future__ import print_function
from ast import Break
import datetime
import os
import smtplib
import sys
from sys import exit
from threading import main_thread
from unittest import result
import webbrowser
from pip import main
from PyQt5.QtCore import pyqtSignal
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from Techsaui import Ui_TECHSA

engine = pyttsx3.init('sapi5')
engine. setProperty("rate", 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning everyone ")

        elif hour>=12 and hour<18:
            speak("Good Afternoon everyone!")   

        else:
            speak("Good Evening everyone") 

        speak("let me introduce me. Im Techsa just an ai. i can do many functions. just as other assistants but not too much. so. how can i help you all!")       

    def takeCommand(self):
        

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")
        return self.query



    def TaskExecution(self):
        self.wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on self.self.query
            if 'meaning of' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)


            

            elif 'thank you' in self.query:
                print("You Are always welcome")
                speak("You Are always welcome")

            
            elif 'open youtube' in self.query:
                speak("opening youtube")
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in self.query:
                googlepath='C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(googlepath)

            elif 'open stack overflow' in self.query:
                speak("opening stack overflox")

                webbrowser.open("https://stackoverflow.com/")  

            elif 'open whatsapp' in self.query:
                webbrowser.open("https://web.whatsapp.com/")
                speak("opening whatsapp") 


            elif 'music' in self.query:
                music_dir = 'C:\Dayal\Songs\ALL'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f" the time is {strTime}")

            elif 'open code' in self.query:
                codePath = ""
                os.startfile(codePath)


            elif 'open amazon' in self.query:

                speak("amazon")
                speak("opening amazon")
                webbrowser.open("https://www.amazon.com/")

            elif 'open GitHub' in self.query:
                speak("opening github")
                webbrowser.open("https://github.com/")

            elif 'open netflix' in self.query:

                speak("opening netflix")
                webbrowser.open("https://www.netflix.com/")


            elif 'prime video' in self.query:

                speak("opening prime video")
                webbrowser.open("https://www.primevideo.com/")

            elif 'hotstar' in self.query:

                speak("opening hotstar")
                webbrowser.open("https://www.hotstar.com/")

            elif 'facebook' in self.query:
                speak("opening facebook")
                webbrowser.open("https://www.facebook.com/")
        

            elif 'instagram' in self.query:

                speak("opening instagram")
                webbrowser.open("https://www.instagram.com/")

            elif 'discord' in self.query:

                speak("opening discord")
                webbrowser.open("https://discord.com/")

            elif 'steam' in self.query:

                speak("opening steam")
                webbrowser.open("https://store.steampowered.com/")

            elif 'roblox' in self.query:

                speak("opening roblox")
                webbrowser.open("https://www.roblox.com/")

            elif 'open stack overflow' in self.query:

                speak("opening stack overflow")
                webbrowser.open("https://stackoverflow.com/")

            elif 'open notepad' in self.query: 
                speak("opening notepad")

                os.startfile("C:\\Windows\\system32\\notepad.exe")



            elif 'school portal' in self.query:
                speak("opening school portal")

                webbrowser.open("https://www.gems.ae/")


            elif 'school website' in self.query:
                speak("opening website")

                webbrowser.open("https://www.gemsoo-alquoz.com/en")



            elif 'exit' in self.query:
                
                print(" have a nice day")   
                speak("You are always welcome, have a nice day")
                quit()




startExecution = MainThread()


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_TECHSA()
        self.ui.setupUi(self)


        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):

        self.ui.movie = QtGui.QMovie("C:\\Dayal\\Python\\TECHSA\\VOICE REG.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):

        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        labelDate = currentTime.toString('hh:mm:ss')
        labelTime = currentDate.toString(Qt.ISODate)
        self.ui.textBrowser.setText(f"Date: {labelTime}")
        self.ui.textBrowser_2.setText(f"Time: {labelDate}")



        i = " "


app = QApplication(sys.argv)
techsa = Main()
techsa.show()
sys.exit(app.exec_())




