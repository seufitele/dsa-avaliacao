
from random import random
from random import randint
import pickle


#Parte que lê o arquivo
def lerArquivo(caminhoArquivo):
    arquivo = open(caminhoArquivo, encoding="utf8") #assume que a codificacao e utf8
    dadosArquivo = arquivo.read()
    arquivo.close()

    return dadosArquivo


def cleanLine(theLine):

        #   $c = comma
        #   $d = dot
        #   $d = dot dot dot
        #   $0 = start
        #   $$$ = cardinality

        #somaTokens = "$$$"

    linhaAtual = theLine.strip().lower()
    linhaAtual = linhaAtual.replace(",", " $c") #da um espaco para contar como um novo token
    linhaAtual = linhaAtual.replace("...", " $ddd ") #da um espaco para contar como um novo token
    linhaAtual = linhaAtual.replace("..", " $ddd ") #da um espaco para contar como um novo token
    linhaAtual = linhaAtual.replace(".", " $d") #transforma num caracter especial (fim de linha)
    linhaAtual = linhaAtual.replace("?", " $d") #transforma num caracter especial (fim de linha)
    linhaAtual = linhaAtual.replace("!", " $d") #transforma num caracter especial (fim de linha)

    linhaAtual = linhaAtual.replace("-", "")
    linhaAtual = linhaAtual.replace("\"", "")

    linhaAtual = "$0 " + linhaAtual     

    return linhaAtual


#Cria um dicionario de markov de ordem 0, ou seja, considerando apenas a palavra atual para 
#descobrir a proxima
def criarDicionario(dados):   

    dict = {}  #dicionario de probabilidades

    #assume que dados é um conjunto de linhas não vazio
    for linha in dados.split('\n'):

        linhaAtual = cleanLine(linha)

        #divide a linha em palavras, removendo as palavras vazias
        tokens = list(filter(lambda ele : len(ele.strip()) != 0, linhaAtual.split(" ")))

        #inicia no 1 porque vamos pegar a palavra anterior
        for idx in range(1, len(tokens)):
        
            prevToken = tokens[idx-1]
            prevChain = dict.get(prevToken)

            #se nao existe esse valor no dicionario, o cria
            if prevChain == None:
                prevChain = {}
                dict[prevToken] = prevChain

            curToken = tokens[idx].strip()
            curValue = prevChain.get(curToken, 0)

            #curSum = prevChain.get(somaTokens, 0)

            prevChain[curToken] = curValue + 1 #incrementa a ocorrencia do token
            #prevChain[somaTokens] = curSum + 1 #incrementa a ocorrencia do token

    return dict


#gera uma frase a partir do dicionario
def gerarPalavra(dict, curWord):

    possibleStates = dict.get(curWord)
    totalOcc = sum(map(lambda chave : possibleStates.get(chave), possibleStates.keys()))

    #a palavra que vamos buscar
    randomState = randint(1, totalOcc) 

    stateSum = 0

    for state in possibleStates:

        stateSum = stateSum + possibleStates.get(state)

        if (stateSum >= randomState):
            return state

    raise "Erro - não deveria chegar até aqui"

def gerarFrase(dict):

    palavras = []

    palavraAnterior = "$0"
    palavraAtual = gerarPalavra(dict, palavraAnterior)

    while (palavraAtual != "$d"):

        palavras.append(palavraAtual)
        palavraAnterior = palavraAtual
        palavraAtual = gerarPalavra(dict, palavraAnterior)
    

    return palavras

arquivo = "./corpus/composite.txt"
dicionario = criarDicionario(lerArquivo(arquivo))
print(gerarFrase(dicionario))

