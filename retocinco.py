def calcularCosto(alto,ancho,profundo):

    volumen= alto * ancho * profundo
    costo = volumen * 5
    if alto > 30:
        costo+=2000
    if costo > 10000:
        costo*=1.19
    
    return costo

def costoTotal(listaPaquetes,descuento):
    Total= 0
    for i in listaPaquetes:
        
        alto= i ["ALTO"]
        ancho= i ["ANCHO"]
        profundo= i ["PROFUNDO"]
        
        Total += calcularCosto(alto,ancho,profundo)
        
    return Total *(1 - descuento/100)

import json
with open('paquetes.json') as file:
    empresa = json.load(file)
print (costoTotal(empresa['PAQUETES'], 10))
    