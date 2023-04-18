import random  # Importamos la librería random para generar números aleatorios

# Función para tirar el dado y mostrar el resultado


def tirar_dado(dado):
    resultado = random.randint(1, dado)
    # Se usa f-string para imprimir el resultado de forma más clara y concisa.
    print(f"Resultado del dado {dado}: {resultado}")


# Solicitamos al usuario que ingrese el tipo de dado a tirar
while True:
    # Se agrega un try-except para controlar los errores en caso de que se ingrese un valor no numérico.
    try:
        num = int(input("Ingrese un número entero entre 1 y 10: "))
        except ValueError:
            print("Debes ingresar un número entero")
            else:
                if num in range(1, 11):
                    print(f"El número {num} está dentro del rango permitido")
                    else:
                        print("El número ingresado no está dentro del rango permitido")
                        
                        if otra_vez.lower() != 'si' and otra_vez.lower() != 's':
            break
