
import PyPDF2
import pandas as pd
import os

# Recuperamos la lista de los archivos PDF
path = "../raw_data/"
pdf_list = os.listdir(path)

# Iteramos en cada archivo para extraer las razones de tipo 
# de combustible por modo de transporte por año

for pdf in pdf_list:
    pdfReader = PyPDF2.PdfReader(path + pdf)
 
# printing number of pages in pdf file
print("Son ",len(pdfReader.pages)," paginas")
pages = len(pdfReader.pages)
found = False
page = 59

while not found and page<pages:
    print("Searching on page",page)
    # creating a page object
    pageObj = pdfReader.pages[page]
    # extracting text from page
    txt = pageObj.extract_text()
    if "Domestic Consumption" in txt:
        print("Encontrado...")
        #print(txt)
        rows = txt.split('\n')
        #print(rows)
        found = True
    page+=1


csv = []
year = ""
modos_transporte = ('HIGHWAY ','Light vehicles','Buses','Medium/heavy trucks','NONHIGHWAY','Air','Water','Pipeline','Rail')

modo = 0
for row in txt.split('\n'):
    if modo == len(modos_transporte):
        break
    if row.lstrip(' ').startswith("Domestic Consumption"):
        year = row.lstrip(' ').rstrip(' ').split(",")[1].lstrip(' ')[0:-1]
    if row.lstrip(' ').startswith(modos_transporte[modo]):
        new_raw = row.lstrip(' ').rstrip(' ').replace(", ",",").replace(" ,",",").replace(",","").replace(". ",".").replace(" .",".")
        #Limpieza manual debido al tiempo
        new_raw = new_raw.replace("8 61.7", "861.7")
        _,cols = new_raw.split(modos_transporte[modo])
        new_raw = [modos_transporte[modo]] + " ".join(cols.split()).split(" ")
        csv.append(new_raw)
        modo+=1
    
#print(csv)
#print(len(csv))
#print(csv[0])

df = pd.DataFrame(csv)
df = df.set_index(df.columns[0])
columns = ['Gasoline', 'Diesel_fuel', 'Liquified_petroleum_gas','Jet_fuel','Residual_fuel_oil','Natural_gas', 'Electricity', 'Total']
df.columns = columns
#print(year)
#print(df)
print(year,"ok")

  
        

 




