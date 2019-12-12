
#Markov Chain com N estados anteriores
from random import random
from random import randint
import re


#Parte que lê o arquivo
def lerArquivo(caminhoArquivo):
    arquivo = open(caminhoArquivo, encoding="utf8") #assume que a codificacao e utf8
    dadosArquivo = arquivo.read()
    arquivo.close()

    return dadosArquivo

#Limpa a linha, de acordo com algumas regras
#Eu substitui a pontuação para poder posteriomente 'brincar' com diferentes
#pontuações nas respostas
def cleanLine(theLine):

    #   $c = comma         => significa um separador entre palavras. por agora apenas a virgula
    #   $d = dot           => representa um ponto final
    #   $dd = dot dot      => representa um ponto para uma frase que continua
    #   $ddd = dot dot dot => representa os tres pontos
    #   $0 = start         => caracter marcador do inicio da string

    linhaAtual = theLine.strip().lower()
    linhaAtual = linhaAtual.replace(",", " $c") #da um espaco para contar como um novo token
    linhaAtual = linhaAtual.replace("...", " $ddd ") #da um espaco para contar como um novo token
    linhaAtual = linhaAtual.replace("..", " $ddd ") #da um espaco para contar como um novo token

    #substitui caracteres de fim de linha por marcador de fim da string
    linhaAtual = re.sub("[.!?]$", " $d", linhaAtual)

    linhaAtual = linhaAtual.replace(".", " $dd") #transforma num caracter especial (fim de linha)
    linhaAtual = linhaAtual.replace("?", " $dd") #transforma num caracter especial (fim de linha)
    linhaAtual = linhaAtual.replace("!", " $dd") #transforma num caracter especial (fim de linha)

    linhaAtual = linhaAtual.replace("-", "")
    linhaAtual = linhaAtual.replace("\"", "")

    linhaAtual = "$0 " + linhaAtual     

    return linhaAtual


#Cria um dicionario de markov de ordem n, ou seja, considerando n estados
#para definir a probabilidade do proximo
def criarDicionario(dados, numberStates = 1):   

    dict = {}  #dicionario de probabilidades

    #assume que dados é um conjunto de linhas não vazio
    for linha in dados.split('\n'):

        #limpa a linha antes de prosseguir
        linhaAtual = cleanLine(linha)

        #divide a linha em palavras, removendo as palavras vazias
        tokens = list(filter(lambda ele : len(ele.strip()) != 0, linhaAtual.split(" ")))

        #inicia no 1 porque vamos pegar a palavra anterior
        for idx in range(1, len(tokens)):
        
            #para cada estado anterior, grava as probabilidades
            for idx2 in range(max(0, idx-numberStates), idx):

                #pega o estado anterior como uma 'janela' das palavras observadas
                prevStates = tuple(tokens[idx2:idx])
                prevChain = dict.get(prevStates)

                #se nao existe esse valor no dicionario, o cria
                if prevChain == None:
                    prevChain = {}
                    dict[prevStates] = prevChain

                curToken = tokens[idx].strip()
                curValue = prevChain.get(curToken, 0)

                prevChain[curToken] = curValue + 1 #incrementa a ocorrencia do token

    return dict


#gera uma frase a partir do dicionario.
#prevStates é uma lista de estados anteriores a serem considerados
def gerarPalavra(dict, prevStates):

    possibleStates = dict.get(tuple(prevStates))

    #nao encontrou para essa quantidade de estados, 
    # tenta com menos elementos (descartando o primeiro)
    if possibleStates == None:
        return gerarPalavra(dict, possibleStates[1:])

    #conta quantas variacoes aquele estado possui
    totalOcc = sum(map(lambda chave : possibleStates.get(chave), possibleStates.keys()))

    #gera a probabilidade para descobrir a palavra
    randomState = randint(1, totalOcc) 

    stateSum = 0

    # 'caminha' entre os estados até encontrar a probabilidade correta
    for state in possibleStates:

        stateSum = stateSum + possibleStates.get(state)

        if (stateSum >= randomState):
            return state

    raise "Erro - não deveria chegar até aqui"

#funcao para gerar uma frase a partir de diversas palavras
def gerarFrase(dict, numberStates = 1):

    palavras = []

    prevStates = ["$0"]
    palavraAtual = gerarPalavra(dict, prevStates)

    #continua ate encontrar o token de fim de palavra
    while (palavraAtual != "$d"):

        palavras.append(palavraAtual)
        prevStates.append(palavraAtual)
        prevStates = prevStates[max(len(prevStates) - numberStates, 0):]
        palavraAtual = gerarPalavra(dict, prevStates)
    
    return palavras


arquivo = "./corpus/composite.txt"
dicionario = criarDicionario(lerArquivo(arquivo), 3)
print(gerarFrase(dicionario, 3))

