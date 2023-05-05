from Modo.Combates.muerte import Muerte
from Modo.Combates.impros import Impros
from Modo.Combates.magios import Magios
from Modo.Combates.forzudos import Forzudos

class Modo:
    
    def modo_combate(self):
        print("MODO COMBATE")
        print("""
El modo Combate tiene 2 modos :V 
1. Lucha a MUERTE
2. Lucha Contra los FORZUDOS
3. Lucha contra los MAGIOS
4. Lucha contra los IMPROS
5. ATRAZ       
""")
        
        Lucha = input("Ingresa tu elección: ")

        if Lucha.lower() == "1" or Lucha.lower()=="MUERTE":
            print("Escogiste la opcion")
            muerte = Muerte()


        elif Lucha.lower() == "2" or Lucha.lower()=="FORZUDOS":
            print("Escogiste la opcion")
            forzudos = Forzudos()
            forzudos.mostrar_habilidades()

        elif Lucha.lower() == "3" or Lucha.lower()=="MAGIOS":
            print("Escogiste la opcion")
            magios = Magios()
            magios.mostrar_habilidades()

        elif Lucha.lower() == "4" or Lucha.lower()=="IMPROS":
            print("Escogiste la opcion")
            impros = Impros()
            impros.mostrar_habilidades()        

        elif Lucha.lower() == "5" or Lucha.lower()=="ATRAZ":
            print("No hay ningún atrás a donde volver muajajajaja")
            self.modo_combate()

        else:
            print("\nOpción inválida. Intenta de nuevo.\n")
            self.modo_combate()
            pass

    def modo_historia(self):
        print("MODO HISTORIA")
        pass

    def Salir(self):
        print("Salientod")
        pass