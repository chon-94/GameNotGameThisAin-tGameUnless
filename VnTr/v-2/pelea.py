import random

class Pelea:
    def __init__(self, jugador, enemigo):
        self.jugador = jugador
        self.enemigo = enemigo
        
    def iniciar_pelea(self):
        print("\nInicia la pelea entre", self.jugador.nombre, "y", self.enemigo.nombre)
        
        while self.jugador.vida > 0 and self.enemigo.vida > 0:
            print("¿Qué acción quieres realizar?")
            print("1. Luchar (Fuerza)")
            print("2. Hechizar (Inteligencia)")
            print("3. Engatusar (Carisma)")
            print("4. Salir corriendo")
            
            opcion = input("\nIngresa el número de la opción que quieres realizar: ")
            
            if opcion == "1":
                ataque = self.jugador.fuerza
                defensa = self.enemigo.fuerza
                
                print(self.jugador.nombre, "usa su fuerza para atacar a ", self.enemigo.nombre)
                print(self.enemigo.nombre, "recibe", ataque, "de daño")
                
            elif opcion == "2":
                ataque = self.jugador.inteligencia
                defensa = self.enemigo.inteligencia
                
                print(self.jugador.nombre, "usa su inteligencia para atacar a ", self.enemigo.nombre)
                print(self.enemigo.nombre, "recibe", ataque, "de daño")
                
            elif opcion == "3":
                ataque = self.jugador.carisma
                defensa = self.enemigo.carisma
                
                print(self.jugador.nombre, "usa su carisma para atacar a ", self.enemigo.nombre)
                print(self.enemigo.nombre, "recibe", ataque, "de daño")
                
            elif opcion == "4":
                print(self.jugador.nombre, "sale corriendo de la pelea!")
                break
                
            else:
                print("Opción inválida, intente de nuevo.")
                continue
            
            self.enemigo.vida -= ataque
            if self.enemigo.vida <= 0:
                print(self.enemigo.nombre, "ha sido derrotado!")
                break
            
            print(self.enemigo.nombre, "contraataca!")
            ataque_enemigo = random.randint(1, defensa)
            print(self.enemigo.nombre, "usa un ataque con fuerza", ataque_enemigo)
            self.jugador.vida -= ataque_enemigo
            
            if self.jugador.vida <= 0:
                print('\n'+self.jugador.nombre, "ha sido derrotado!")
                break
                
            self.jugador.mostrar_habilidades()
            self.enemigo.mostrar_habilidades()
            
        print("Fin de la pelea.\n")
