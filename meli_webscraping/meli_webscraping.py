# -*- coding: utf-8 -*-

"""
Proyecto personal

#####################

Web scraping con API de MELI
############################

@author: Facundo Valle Quintana


"""

"""
Importamos paquetes

"""
import time
import csv
import requests

# Al usar la API tenemos que seguir este formato:
# https://api.mercadolibre.com/sites/$SITE_ID/search?q=nombre%20item

# Notar que:
# $SITE_ID: MLA  # MLA es el sitio de Argentina
# item: item a buscar. (reemplazamos los espacios con %20)

buscar = "Toyota SW4"
url = "https://api.mercadolibre.com/sites/{}/search?q={}".format("MLA", buscar.replace(" ", "%20"))

# Hacemos el pedido o request y obtenemos la response
response = requests.request("GET", url)
print(response) # correcto

# Vemos el texto
response.text

# Guardamos resultado en un diccionario

data = response.json()

print(data)

# Obtenemos el precio y el link del primer resultado de la búsqueda

print('Precio del primer resultado:', data['results'][0]['price'])
print(data['results'][0]['permalink'])