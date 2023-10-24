from bs4 import BeautifulSoup
from requests_html import HTMLSession
import time
import re

session = HTMLSession()
r = session.get("https://es.wallapop.com/coches-segunda-mano/furgonetas")
r.html.render()
soup = BeautifulSoup(r.content,"html.parser")
texto = soup.text
texto = texto.split("Novedades")
texto = texto[1]

pointers = [m.start() for m in re.finditer("EUR",texto)]

pointerinit = 0
anuncios = []
for pointer in pointers:
    pointer = pointer -9
    anuncios.append(texto[pointerinit:pointer])
    pointerinit = pointer

######################

newanuncios = []
for anuncio in anuncios:  
    anuncio:str = anuncio
    anuncio = anuncio.split("     ")

    newanuncio = []     
    for element in anuncio:
         
        if element != "" and element != " \n":
            newanuncio.append(element)
        try:
            price:str = newanuncio[0]
            price = price.lstrip()
            price = price.replace("\n","")

            model:str = newanuncio[1]
            model = model.lstrip()
            model = model.replace("\n","")

            description = str
            description = str(newanuncio[2])
            description = description.lstrip()
            description = description.replace("\n","")

        except:pass
    newanuncios.append((price,model,description))


print(newanuncios[5])


    #print(price)
print("-------------------")




"""pointer = texto.find("EUR")
pointer = pointer -9

lista = (texto[0:pointer])


price = (texto[pointer:pointer+15])
price = price.rstrip()
price = price.lstrip()


print(price)"""

"""listadetextos = []
for texto in textos:
    if texto != "":
        listadetextos.append(texto)"""

"""for n,texto in enumerate(listadetextos):
    if "EUR" in texto:
        print (n)
        print(texto)
"""

"""print ({"value":listadetextos})"""