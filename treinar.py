#-*- coding: utf-8 -*-
                                                                          
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import os

bot = ChatBot('Tot')

#treinar Tot
bot.set_trainer(ListTrainer)

for arquivo in os.listdir('conversas'): #percorrer todos os aquivos do diretório 
    linhas = open('conversas/'+ arquivo, 'r').readlines() #ler as linhas do arquivo 

    bot.train(linhas)