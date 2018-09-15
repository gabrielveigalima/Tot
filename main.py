# encoding: utf-8
                                                                          
#from chatterbot.trainers import ListTrainer
#from chatterbot import ChatBot

import os

import pyaudio
import speech_recognition as sr

#bot = ChatBot('Tot', read_only=True)

""" treinar Tot
bot.set_trainer(ListTrainer)

for arquivo in os.listdir('conversas'): #percorrer todos os aquivos do diretório 
    linhas = open('conversas/'+ arquivo, 'r').readlines() #ler as linhas do arquivo 

    bot.train(linhas)"""


# pega audio pelo microfone


r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Tot disse: Fala meu Padrinho!\nEstou ouvindo... :)\nCaso queria sair, diga 'tchau Tot'")

    while True:
        audio = r.listen(source)
        #try:
        fala = r.recognize_google(audio, language='pt')
        """if(fala.lower() == 'tchau tot' or fala.lower() == 'tchau toddy' or fala.lower() == 'tchau' or fala.lower() == 'tchau totti'):
            print('Tot disse: Tchau... :)')
            break
        else:"""
        print("Você disse: " + fala)  
        print("Tot disse: " + bot.get_response(fala))      
        """except sr.UnknownValueError:
            print('Tot disse: Não foi possível entender o áudio')
        except sr.RequestError as e:
            print('Tot disse: Não foi possível solicitar resultados. {0}'.format(e))"""
