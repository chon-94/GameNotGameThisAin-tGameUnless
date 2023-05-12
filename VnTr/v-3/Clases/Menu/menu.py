from Clases.enemigo import Enemigo

class Menu:# Menu

    def mostrar_menu(self):# 6 o 7 opciones
        print("\n¡Bienvenido al Menú de Opciones!")
        print("1. Combate a Muerte")
        print("2. Combate a Fuerza")
        print("3. Combate a Carisma ")
        print("4. Combate a Inteligneca")
        print("5. Historia x")
        print("6. Salir")

    def ejecutar_menu(self):# Opciones

        while True:# Bucle infinito con condicion true
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción:\n")

            if opcion.lower() == "1" or opcion.lower() =="combate muerte":
                opciones = Enemigo(1)
                opciones.generar_combate_habilidad_aleatoria()

            elif opcion.lower() == "2" or opcion.lower() =="combate fuerza" or opcion.lower() =="fuerza":
                opciones = Enemigo(2)
                opciones.generar_combate_fuerza_aleatoria()
            
            elif opcion.lower() == "3" or opcion.lower() =="combate carisma" or opcion.lower() =="carisma":
                opciones = Enemigo(3) 
                opciones.generar_combate_carisma_aleatoria()
            
            elif opcion.lower() == "4" or opcion.lower() =="combate inteligencia" or opcion.lower() =="inteligencia":
                opciones = Enemigo(4) 
                opciones.generar_combate_inteligencia_aleatoria()
            
            elif opcion.lower() == "5" or opcion.lower() =="Historia ":
                print("\nhistoria americana ekis donde sale el herma de risde malcom el del medio\n")

            elif opcion.lower() =="combate":
                print('Combates es bacan')
                continue
        
            elif opcion.lower() == "6" or opcion.lower() =="Salir ":
                print("\nSaliendo del programa...")
                break            
    
            else:
                print("\nOpción inválida. Intente nuevamente.\n")
                continue

