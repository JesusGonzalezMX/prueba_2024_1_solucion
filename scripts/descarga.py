"""Descarga de la información
Este scrip permite al usuario descargar los recursos que contienen la 
información acerca del Consumo doméstico de energía de transporte por 
modo y tipo de combustible de 2008 a 2019, descargando las ediciones 
28 a 40 del Transportation Energy Data Book (TEDB).
"""

import requests
from bs4 import BeautifulSoup

def get_links():
    """Regresa una lista de los enlaces a las ediciones 28 a 40 del 
    Transportation Energy Data Book (TEDB) y una lista de los nombres
    de estos archivos.

    Parameters
    ----------
    None

    Returns
    -------
    list
        Una lista de enlaces a archivos pdf
    """
    #El primer pdf es la edicion 40 y no esta en los archivos por lo 
    #que la agregamos manualmente
    print("Obteniendo links...")
    print("Transportation Energy Data Book: Edition 40")
    names = ["TEDB_40"]
    links = ['https://tedb.ornl.gov/wp-content/uploads/2022/03/TEDB_Ed_40.pdf']
    #Las demas ediciones las obtenemos del archivo
    archive_url = 'https://tedb.ornl.gov/archive/'

    reqs = requests.get(archive_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        if link.text.startswith("T") and int(link.text[-2:])>27:
            print(link.text)
            names.append("TEDB_"+link.text[-2:])
            links.append(link.get('href'))
    return links,names

def download_files(links:list,names:list)->None:
    """Descarga las ediciones 28 a 40 del Transportation 
        Energy Data Book (TEDB) en la carpeta raw_data.

    Parameters
    ----------
    links : list
        links a archivos pdf
    names : list
        nombres de los archivos pdf
    Returns
    -------
    None
    """
    print("Descargando recursos...")
    for i,link in enumerate(links):
        # Get response object for link
        response = requests.get(link)
        # Write content in pdf file
        pdf = open("../data/raw_data/" + names[i]+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        print(names[i], " descargado")
  
    print("Se ha completado la descarga de informacion")



download_files(*get_links())


