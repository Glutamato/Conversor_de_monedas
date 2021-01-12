Bolivares= input("¿Cuántos Bolívares tienes disponible?: ")
Bolivares= float(Bolivares)
Valor_dolar= input("¿A cuánto está cotizando el dolar?: ")
Valor_dolar= float(Valor_dolar)
Dolares=Bolivares/Valor_dolar
Dolares=round(Dolares,0)
Dolares=str(Dolares)
print("Tienes $" + Dolares + " dólares")
