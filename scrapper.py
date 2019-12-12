from bs4 import BeautifulSoup
import requests

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

        #print(piada)

arquivo.close()