def calcularCosto(alto,ancho,profundo):

    volumen= alto * ancho * profundo
    costo = volumen * 5
    if alto > 30:
        costo+=2000
    if costo > 10000:
        costo*=1.19
    
    return costo


def costoTotal(numeroPaquetes,descuento):
    Total= 0
    for i in range(numeroPaquetes):
        
        alto= float(input())
        ancho= float(input())
        profundo= float(input())
        
        Total += calcularCosto(alto,ancho,profundo)
        
    return Total *(1 - descuento/100)

print(costoTotal(2, 50))
print(calcularCosto(35,10,5))
