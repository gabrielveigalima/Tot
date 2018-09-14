# encoding: utf-8
                                                                          
import pyaudio
import speech_recognition as sr
fala = "sim".upper()
# pega audio pelo microfone
r = sr.Recognizer()
with sr.Microphone() as source:

    print("Olá!\nEstou ouvindo... :)\nCaso queria sair, diga 'sair'")

    audio = r.listen(source)
try:
    fala = r.recognize_google(audio, language='pt')
    print("Você disse " + fala)
    
except sr.UnknownValueError:

    print("Não foi possível entender o áudio")
except sr.RequestError as e:
    print("Não foi possível solicitar resultados. {0}".format(e))
