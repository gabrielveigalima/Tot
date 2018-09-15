# encoding: utf-8
                                                                          
import pyaudio
import speech_recognition as sr
fala = "sim".upper()
# pega audio pelo microfone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Tot disse: Fala meu Padrinho!\nEstou ouvindo... :)\nCaso queria sair, diga 'tchau Tot'")

    while True:
        audio = r.listen(source)
        try:
            fala = r.recognize_google(audio, language='pt')
            if(fala.lower() == 'tchau tot' or fala.lower() == 'tchau toddy' or fala.lower() == 'tchau' or fala.lower() == 'tchau totti'):
                print('Tot disse: Tchau... :)')
                break
            else:
                print("Você disse: " + fala)
            
        except sr.UnknownValueError:
            print('Tot disse: Não foi possível entender o áudio')
        except sr.RequestError as e:
            print('Tot disse: Não foi possível solicitar resultados. {0}'.format(e))
