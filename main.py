# encoding: utf-8
                                                                          
import pyaudio
import speech_recognition as sr

# pega audio pelo microfone
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Estou ouvindo... :)")
    audio = r.listen(source)   
try:
    print("Você disse " + r.recognize_google(audio, language='pt'))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
