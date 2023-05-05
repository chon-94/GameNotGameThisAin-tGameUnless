from personaje import Personaje
#from enemigo import Enemigo
from Modo.modo import Modo

class Main:

    def __init__(self):
        
        self.personaje = Personaje()
#        self.enemigo = Enemigo()
        self.modo = Modo()
        #self.combate = Combate(Personaje, enemigo, num_peleas)

    def iniciar_juego(self):
        print("\n¡Comienza el juego!")
        self.personaje.puntos_cif()
        print("\n¡ESTAS NOS LAS CARACTERISTICAS!")        
        self.personaje.mostrar_habilidades()
#        self.enemigo.mostrar_habilidades()
        
        while True:
            print("""
                Selecciona la opcion que quieras
                1. Combates 
                2. Historia
                3. Salir
                """)    
            
            opcion = input("Ingresa tu elección: ")

            if opcion == "1":
                self.modo.modo_combate()
                continue

            elif opcion == "2":
                self.modo.modo_historia()
                continue

            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")

juego = Main()# Creamos una instancia de la clase Main

juego.iniciar_juego()# Iniciamos el juego llamando al método iniciar_juego de la instancia de Main