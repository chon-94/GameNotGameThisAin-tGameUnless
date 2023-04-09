import random  # Importamos la librería random para generar números aleatorios

# Función para tirar el dado y mostrar el resultado
def tirar_dado(dado):
    resultado = random.randint(1, dado)
    print("Resultado del dado " + str(dado) + " : " + str(resultado))

# Solicitamos al usuario que ingrese el tipo de dado a tirar
while True:
    try:
        dado = int(input("Ingrese el tipo de dado a tirar (4, 6, 8, 10, 12, 120): "))
        if dado in [4 ,6 ,8 ,10 ,12 ,120 ]:
            tirar_dado(dado)
        else:
            print("ehhh si mira tienes que ingresar solo un mero que salga en la lista")
    except ValueError:
        print("perondon pero acabas de ingresar una letra...? ")
    otra_vez = input("¿Otro intento? (si/no): ")
    if otra_vez.lower() != 'si' and otra_vez.lower() != 's':
        break

    