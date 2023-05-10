from opciones import Opciones

class Menu:

    def mostrar_menu(self):
        print("\n¡Bienvenido al Menú de Opciones!")
        print("1. Combate a Muerte")
        print("2. Combate a Fuerza")
        print("3. Combate a Magia")
        print("4. Combate a Carisma")
        print("5. Historia x")
        print("6. Salir")

    def ejecutar_menu(self):

        while True:

            self.mostrar_menu()
            opcion = input("\nSeleccione una opción:\n")

            if opcion.lower() == "1" or opcion.lower() =="combate muerte":
                opciones = Opciones()
                opciones.combate_muerte()

            elif opcion.lower() == "2" or opcion.lower() =="combate fuerza":
                opciones = Opciones()
                opciones.combate_fuerza()
            
            elif opcion.lower() == "3" or opcion.lower() =="combate carisma":
                opciones = Opciones()
                opciones.combate_carisma()
            
            elif opcion.lower() == "4" or opcion.lower() =="combate inteligencia":
                opciones = Opciones()
                opciones.combate_inteligencia()
            
            elif opcion.lower() == "5" or opcion.lower() =="Historia ":
                opciones = Opciones()
                opciones.historia_x()
            
            elif opcion.lower() == "6" or opcion.lower() =="Salir ":
                print("\nSaliendo del programa...")
                break            
            
            else:
                print("\nOpción inválida. Intente nuevamente.\n")
                continue

