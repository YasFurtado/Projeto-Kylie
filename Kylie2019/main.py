from Chatbot import Chatbot
#-*- coding: utf-8 -*-

Bot = Chatbot("Kylie")
print('Seja bem-vindo ao programa Kylie')
print('---DIGITE oi PARA INICIAR---')
#while infinito do programa. Se encerra com uma despedida.
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    #Resolvido hehe
    if  resp == 'Tchau':
        break
    
