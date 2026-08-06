"""Programa principal del proyecto modular BCCR."""

from lectura_datos  import cargar_tabla_bccr, mostrar_top_10
from limpieza_datos import limpiar_datos, filtrar_diferencial_alto, resumir_por_tipo_entidad


def ejecutar():
    """cargar los datos y presentar el menu del sistema"""
    datos_brutos = cargar_tabla_bccr()
    datos = limpiar_datos(datos_brutos)
    
    
    
    while True:
        print("\n Proyecto de analisis de BCCR:")
        print("1. mostrar las primeras 10 entidades")
        print("2. promedio por tipo de netidad")
        print("3. mostar entidades financiertas con diferencil mayo al promedio")
        print("4. mostrar lista de entidades y exportar a un csv")
        print("5. graficar")
        print("6. salir")
        opcion = input("Seleccione una opción: ")




        if opcion == "1": 
            
            print(mostrar_top_10(datos))
        elif opcion == "2":
            promedios = resumir_por_tipo_entidad(datos)
            print(f"Promedio general del diferencial: {promedios[0]:.2f}")
            print(promedios[1].to_string(index=False))
        elif opcion == "3":
            print("Entidades con diferencial mayor al promedio:")
            entidades_altas = filtrar_diferencial_alto(datos)
            print(mostrar_top_10(entidades_altas))
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":    
            print("Saliendo del analisis...")   
            input("Presione Enter para salir...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            print("\n")
    
    
if __name__ == "__main__":
    ejecutar()
    