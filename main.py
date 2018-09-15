#-*- coding: utf-8 -*-
                                                                          
from chatterbot import ChatBot

import pyaudio
import speech_recognition as sr
import pyttsx3

voz = pyttsx3.init('sapi5');

bot = ChatBot('Tot', read_only=True)


def falar(texto):
    voz.say(texto)
    voz.runAndWait()

# pega audio pelo microfone

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Tot disse: Fala meu Padrinho!\nEstou ouvindo... :)\nCaso queria sair, diga 'tchau Tot'")
    falar('Fala meu Padrinho! Estou ouvindo, caso queria sair, diga tchau Tot')
    while True:
        audio = r.listen(source)
        try:
            fala = r.recognize_google(audio, language='pt')
            if(fala.lower() == 'tchau tot' or fala.lower() == 'tchau toddy' or fala.lower() == 'tchau' or fala.lower() == 'tchau totti'):
                print('Tot disse: Tchau Padrinho... :)')
                falar('Tchau padrinho')
                break
            else:
                print('Você disse: {0}'.format(fala))  
                respostaTot = bot.get_response(fala)
                falar(respostaTot)
                print('Tot  disse: {0}'.format(respostaTot))      
        except sr.UnknownValueError:
            print('Tot disse: Não foi possível entender o áudio')
            falar('Não foi possível entender o áudio')
        except sr.RequestError as e:
            falar('Não foi possível entender o áudio, deu erro')
            print('Tot disse: Não foi possível solicitar resultados. {0}'.format(e))
