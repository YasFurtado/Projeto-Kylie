#função para capturar resto do usuário e corrigir as respostas recebidas
def resposta():
    resp = input ('>: ')
    resp = resp.lower() #metódo para variações de maisculo e minúsculo
    resp = resp.replace ('eh', 'é') #método para vícios de linguagem
    return resp

#início das variações de nome
def pegaNome(nome):
    if 'o meu nome é' in nome:
        nome = nome[13:]
    elif 'eu me chamo' in nome:
        nome = nome[12:]
    elif 'meu nome é' in nome:
        nome = nome[11:]
    elif 'yo me llamo' in nome:
        nome = nome[12:]
    nome = nome.title()
    return nome

#Respostas ao nome
def respondeNome(nome):
    conhecidos = ['Ian', 'Mário','Heloisa', 'Júlia', 'Davi','Antonia']
    dona = ['Yasmim', 'yas', 'Yas', 'yasmim']

    if nome in dona:
        frase=( 'K: É bom revê-la, '+nome+'!')
        
    elif nome in conhecidos:
        frase=('K: É muito bom te ver novamente, '+nome+'!')

    else:
        frase= ('É um prazer, '+nome)
           
    return(frase)


        
