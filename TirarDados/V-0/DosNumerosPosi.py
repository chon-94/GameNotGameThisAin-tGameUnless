numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
    
# Mejorado 
while True: 

    try: 
        numero = int(input("Ingrese un número: ")) 
        if numero > 0: 
            print("El número es positivo") 

        elif numero < 0: 
            print("El número es negativo")

        else: 
            print("El número es cero")

        break

    except ValueError:  # Control de errores en caso de que se ingrese un valor no numérico.  

        print('Por favor, ingresa un valor numérico.')