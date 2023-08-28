from contador import Contador
from menu import Menu
from decimal1 import Decimal
from hexa import Hexadecimal
from octal import Octal
from binario import Binario

def main():
    contador = Contador()
    menu = Menu()

    menu.mostrar_menu()
    opcion_sistema = input("Elige un sistema (1/2/3/4): ")
    
    if opcion_sistema == "1":
        sistema = Decimal()
    elif opcion_sistema == "2":
        sistema = Hexadecimal()
    elif opcion_sistema == "3":
        sistema = Octal()
    elif opcion_sistema == "4":
        sistema = Binario()
    else:
        print("Opción no válida. Elige 1, 2, 3 o 4.")
        return
    
    while True:
        print(f"Valor actual ({sistema.__class__.__name__}):")
        print(sistema.obtener_valor())
        
        print("\nElige una opción:")
        print("1. Incrementar")
        print("2. Cambiar sistema")
        print("3. Salir")
        
        opcion = input()
        
        if opcion == "1":
            sistema.incrementar()
        elif opcion == "2":
            opcion_sistema = input("Elige un sistema (1/2/3/4): ")
            
            if opcion_sistema == "1":
                sistema = Decimal()
            elif opcion_sistema == "2":
                sistema = Hexadecimal()
            elif opcion_sistema == "3":
                sistema = Octal()
            elif opcion_sistema == "4":
                sistema = Binario()
            else:
                print("Opción no válida. Elige 1, 2, 3 o 4.")
                continue
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Introduce 1, 2 o 3.")

if __name__ == "__main__":
    main()
