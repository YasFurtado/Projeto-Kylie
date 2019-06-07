import json #importando o json
import sys 
import os 
import subprocess as s
#-*- coding: utf-8 -*-

class Chatbot():
    
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')#abrindo a memória da Kylie
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('[["Ian", "Yasmim", "Yas", "Heloisa"],{"oi": "Olá, qual o seu nome?", "bom dia": "Bom dia!", "qual o seu nome?": "Meu nome é Kylie", "boa tarde": "Boa tarde!"}]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
            
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None, ] 

    def escuta(self):# função que recebe os inputs do usuário
        frase = input ('>: ')
        frase = frase.replace ('eh', 'é') #método para vícios de linguagem
        return frase
    
    def pensa(self, frase): # função que analisa a frase
        if frase in self.frases:
            return self.frases[frase] 
        
        if frase== 'aprende': # condição para criar novas respostas e perguntas à Kylie
            chave = input ('Digite a frase: ')
            resp = input ('Digite a resposta: ')
            self.frases[chave] = resp
            self.gravaMemoria()
            return 'Aprendido'

        if self.historico [-1] == 'Olá, qual o seu nome?': 
            nome = self.pegaNome(frase)
            frase= self.respondeNome(nome)
            return frase
        try:
            resp = str(eval(frase)) #resolver cálculos matematicos
            return resp
        except:
            pass
        
        return 'Não entendi'
        
            
    def pegaNome(self, nome):
        if 'o meu nome é' in nome.lower():# separa o resto da frase e concatena só o nome
            nome = nome[13:]
        elif 'eu me chamo' in nome.lower():
            nome = nome[12:]
        elif 'meu nome é' in nome.lower():
            nome = nome[11:]
        elif 'yo me llamo' in nome.lower():
            nome = nome[12:]
        elif 'me chamo' in nome.lower():
            nome = nome[9:]
        elif 'me chamam' in nome.lower():
            nome = nome[10:]
        elif 'me chame de' in nome.lower():
            nome = nome[12:]
        elif 'me chame' in nome.lower():
            nome = nome[9:]
        elif 'o nome que me foi dado é' in nome.lower():
            nome = nome[25:]

        nome = nome.title()#deixa o nome com a primeira letra maiúscula
        return nome


#Respostas do programa 
    def respondeNome(self, nome):

        if nome in self.conhecidos: # Se o nome for conhecido, executa isso
            frase=('K: É muito bom te ver novamente, '+nome+'!')
        else: #Se o nome não for conhecido, ele será adicionado ao arquivo json
            frase= ('É um prazer, '+nome)
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase

    

    def gravaMemoria(self):
        memoria = open(self.nome+'.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()



    def fala(self, frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                os.startfile(comando)

        else:
            print(frase)#respostas
        self.historico.append(frase)#adiciona ao histórico

        




