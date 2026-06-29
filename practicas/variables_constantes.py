# programa para calcular el area de un circulo
# Adonis Roman
# Entradas
PI = 3.1416 # LA VARiABLE EN MAYUSCULA SON CONSTANTES ES DECIR NO CAMBIAN
#print(type(PI)) #asi se imprime el tipo de variable 
# en este caso seria float
#ejemplo esto solo funciona en phyton 
#PI = "HOla mundo"
#cambiar la variable de typo  puede ser en entero o en string
#print(PI,"tipo de variable", type(PI))
radio = int(input("ingrese el radio de su circulo en cm :"))
area = PI * (radio ** 2)
print("\n")
print(f"su variable es ",radio,"en tipo de la misma es",type(radio))
print(f"-----el area de su circulo es de {area:.2f} cm2-----")
print("\n")
#usar comillas sencillas si se imporime solo 'texto'
# a la par de 0