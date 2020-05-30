today = int(input("Ingrese que dia es hoy: "))

resultado = (today != 15 or 30)

print(resultado)

if resultado == False:
    print("Hoy es quincena")

else:
    print("No es quincena")
    question = input("¿Desea saber cuantos dias faltan para la quincena?: ")
    
    if question == 'si':
        print("Ok")