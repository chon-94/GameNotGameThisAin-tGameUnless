import random  # Genera números aleatorios

def tirar_dado(dado): # Función dado muestra resultado
    resultado = random.randint(1, dado)

    print(f"Resultado del dado {dado}: {resultado}")
    # [[f-string]] imprime resultado de forma más clara y concisa.


while True: # Genera Bucle

    try:# try controla los errores en caso de que se ingrese un valor no numérico.
        dado = int(
            input("\nIngrese el tipo de dado a tirar (4, 6, 8, 10, 12, 120): "))

        # Se cambia la condición para que sea más clara y concisa.
        if dado in [4, 6, 8, 10, 12, 120]:
            tirar_dado(dado)

        else:  # Se agrega un else para mostrar un mensaje en caso de que se ingrese un valor no permitido.
            print("\nehhh si mira tienes que ingresar solo un mero que salga en la lista")

    except ValueError:  # Se agrega un except ValueError para controlar los errores en caso de que se ingrese un valor no numérico.
        print("\nperondon pero acabas de ingresar una letra...? ")

    otra_vez = input("""\n¿Otro intento? 
escribe loque seapara continuar
para salir pon (no): \n""")

    # Se cambia la condición para que sea más clara y concisa.
    if otra_vez.lower() != 'no' and otra_vez.lower() != 'n':
        break
    else:
        break