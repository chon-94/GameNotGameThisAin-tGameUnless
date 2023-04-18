
# Refactorización:
import random  # Importamos la librería random para generar números aleatorios

# Función para tirar el dado y mostrar el resultado
def tirar_dado(dado):
    resultado = random.randint(1, dado)                                                                 
    print(f"Resultado del dado {dado}: {resultado}") # Se usa f-string para imprimir el resultado de forma más clara y concisa. 

# Solicitamos al usuario que ingrese el tipo de dado a tirar
while True:
    try:  # Se agrega un try-except para controlar los errores en caso de que se ingrese un valor no numérico. 
        dado = int(input("Ingrese el tipo de dado a tirar (4, 6, 8, 10, 12, 120): "))

        if dado in [4 ,6 ,8 ,10 ,12 ,120 ]: # Se cambia la condición para que sea más clara y concisa. 
            tirar_dado(dado)

        else:  # Se agrega un else para mostrar un mensaje en caso de que se ingrese un valor no permitido. 
            print("ehhh si mira tienes que ingresar solo un mero que salga en la lista")

    except ValueError:  # Se agrega un except ValueError para controlar los errores en caso de que se ingrese un valor no numérico. 
        print("perondon pero acabas de ingresar una letra...? ")

    otra_vez = input("¿Otro intento? (si/no): ")

    if otra_vez.lower() != 'si' and otra_vez.lower() != 's': # Se cambia la condición para que sea más clara y concisa. 
        break