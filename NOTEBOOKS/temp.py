temperaturas = []
cantidad_registrada = 0

# Complete aquí el ciclo while.

while True:
        print("\n------registro de temperatura------")
        print("1.regiatrar temperatura  ")
        print("2.reporte de temperatura  ")
        print("3. salir   ")
        
        opcion = input ("ingrese una opcion del menu :")
        if opcion == "1":
                temp = float(input("ingrese la temperatura"))
                temperaturas.append(temp)
                print("\n")
                print(f"------registrado con exito-------")
                print("\n")
        elif opcion == "2":
                print("---reporte de temperaturas---")
                print("\n")
                cantidad = len (temperaturas)
                print(f"cantidead de temperaturas rtejistradas : {cantidad}")
                print(f"temperatura maxima : {max(temperaturas)}")
                print(f"temperatura minima :{min(temperaturas)}")
                print(f"temperatura promedio : {sum(temperaturas)/cantidad:.2f}")
        elif opcion == "3":
                print("cerrando aplicacion3")
                break        
        else: 
                print("opcion invalida")
        