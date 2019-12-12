from bs4 import BeautifulSoup
import requests
import re

#codigo para fazer scraping em pagina web

#scraping do  "https://onelinefun.com/"
def scrap():
    
    fileToSave = "scrapper.txt"

    arquivo = open("./scrapper.txt", "w", encoding="utf8")

    for idx in range(1, 533):
        url = "https://onelinefun.com/" + str(idx) + "/"

        print("lendo a pagina ..." + str(idx))

        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")

        joke = content.findAll("div", attrs={ "class" : "o", "itemtype" : "http://schema.org/CreativeWork" } )

        for ele in joke:
            piada = ele.contents[0].text
            arquivo.write(piada)
            arquivo.write("\n")

    arquivo.close()

def scrap2():
    
    fileToSave = "one-liners.txt"
    arquivo = open("./" + fileToSave, "w", encoding="utf8")

    for idx in range(1, 8):
        url = "https://www.rd.com/jokes/one-liners/page/" + str(idx) + "/"
        print("lendo a pagina ..." + str(idx))

        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")

        joke = content.findAll("div", attrs={ "class" : "excerpt-wrapper" } )

        for ele in joke:
            #print(ele)cls
            piada = ele.contents[1].text
            piada = re.sub("@.*", "", piada)
            arquivo.write(piada)
            arquivo.write("\n")

    arquivo.close()


def scrapSimple():
    
    frases = set()

    for idx in range(1, 201):
        url = "http://www.laughfactory.com/jokes/popular-jokes/all-time/" + str(idx) + "/"
        print("lendo a pagina ..." + str(idx))

        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")

        joke = content.findAll("div", attrs={ "class" : "joke-text" } )

        for ele in joke:
            #print(ele)cls
            piada = ele.contents[1].text

            if (len(piada) < 200):
                frases.add(piada.strip())

    fileToSave = "laugthFactory.txt"
    arquivo = open("./" + fileToSave, "w", encoding="utf8")

    for frase in frases:
        arquivo.write(frase)
        arquivo.write("\n")
    arquivo.close()


scrapSimple()