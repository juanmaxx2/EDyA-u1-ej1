from pila import Pila
from pilaEncadenada import PilaA, Celda

if __name__ == "__main__":
    opcion = 0
    while opcion != "3":
        print("\n1. Ingresar una pila secuencial")
        print("2. Ingresar una pila anidada")
        print("3. Salir")
        opcion = input("Ingrese la opcion a realizar:")

        if opcion == "1":
            cant = int(input("\nIngrese la cantidad de componentes:"))
            unaPila = Pila(cant)
            for i in range(cant):
                x = input("Ingrese el dato:")
                unaPila.insertar(x)
            print("\nMostra los elementos de la lista")
            unaPila.mostrar()
            print("\nSuprimiendo un elemento...")
            unaPila.suprimir()
            print("\nMostra los elementos de la lista suprimiendo el ultimo")
            unaPila.mostrar()

        if opcion == "2":
            cant = int(input("\nIngrese la cantidad de componentes:"))
            unaPila = PilaA(cant)
            for i in range(cant):
                x = input("\nIngrese el elemento a ingresar:")
                print("\nEl elemento ingresado es:{}".format(unaPila.Insertar(x)))
            print("\nMostra los elementos de la lista")
            unaPila.Mostrar()
            print("\nSuprimiendo un elemento...")
            print("\nEl elemento suprimido es:{}".format(unaPila.Suprimir()))
            print("\nMostra los elementos de la lista suprimiendo el ultimo")
            unaPila.Mostrar()