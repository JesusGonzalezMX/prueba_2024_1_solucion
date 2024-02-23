
import PyPDF2
import pandas as pd
import os

# Modos de transporte a considerar
modos_transporte = ('HIGHWAY ','Light vehicles','Buses','Medium/heavy trucks','NONHIGHWAY','Air','Water','Pipeline','Rail')
# Tipos de combustible a considerar
columns = ['Gasoline', 'Diesel_fuel', 'Liquified_petroleum_gas','Jet_fuel','Residual_fuel_oil','Natural_gas', 'Electricity', 'Total']
    

# Recuperamos la lista de los archivos PDF
path = "../raw_data/"
pdf_list = os.listdir(path)

# Iteramos en cada archivo para encontrar la 
# pagina donde se encuentra la informacion 
for pdf in pdf_list:
    print(pdf)
    pdfReader = PyPDF2.PdfReader(path + pdf)
    #Numero de paginas
    pages = len(pdfReader.pages)
    print("Son ",len(pdfReader.pages)," paginas")
    #Buscador de pagina
    found = False
    #Empezamos a buscar despues de la tabla de contenidos
    page = 10
    while not found and page<pages:
        #print("Buscando en pagina ",page)
        pageObj = pdfReader.pages[page]
        txt = pageObj.extract_text()
        if "Domestic Consumption" in txt:
            #print("Encontrado...")
            rows = txt.split('\n')
            #print(rows)
            found = True
        page+=1

    # Si no se encuentra informacion se finaliza la ejecucion 
    # para revisar que sucede con ese archivo
    if not found:
        print("NO SE ENCONTRO INFORMACION EN ", pdf)
        break

    # Usamos la pagina encontrada para extraer las razones 
    # de tipo de combustible por modo de transporte por año
    csv = []
    year = ""
    modo = 0
    for row in txt.split('\n'):
        if modo == len(modos_transporte):
            break
        if row.lstrip(' ').startswith("Domestic Consumption"):
            year = row.lstrip(' ').rstrip(' ').split(",")[1].lstrip(' ')[0:-1].replace(" ","")
        if row.lstrip(' ').startswith(modos_transporte[modo]):
            new_raw = row.lstrip(' ').rstrip(' ').replace(", ",",").replace(" ,",",").replace(",","").replace(". ",".").replace(" .",".")
            
            # Limpieza manual debido a problemas encontrados y al tiempo dado para
            # solucionar la prueba
            new_raw = new_raw.replace("8 61.7", "861.7")
            new_raw = new_raw.replace("1520 0.1", "15200.1")

            _,cols = new_raw.split(modos_transporte[modo])
            new_raw = [modos_transporte[modo]] + " ".join(cols.split()).split(" ")
            csv.append(new_raw)
            modo+=1


    df = pd.DataFrame(csv)
    df = df.set_index(df.columns[0])
    columns = [col+"_"+year for col in columns]
    df.columns = columns
    df.to_csv("../data/procesamiento_salidas/datos_anuales/razones_"+year, sep=',', encoding='utf-8')
    print("df para ",year," creado")

  
        

 




