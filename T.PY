import os 
import csv
ARCHIVO = "lista.csv"   

def consultar_saldo():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    with open(ARCHIVO, "r") as archivo:
        lineas = archivo.readlines()[1:] 
        for linea in lineas:
            cedula, nombre, saldo = linea.strip().split(",")
            if nombre.lower() == nombre_cliente.lower():
                print(f"El saldo de {nombre} es {saldo}")
                return
        print("Cliente no encontrado.")


def contar_mayores_50():
    contador = 0
    with open(ARCHIVO, "r") as archivo:
        lineas = archivo.readlines()[1:]
        for linea in lineas:
            _, _, saldo = linea.strip().split(",")
            if float(saldo) > 50:
                contador += 1
    print(f"Número de clientes con saldo mayor a 50: {contador}")


def listar_por_saldo():
    clientes = []
    with open(ARCHIVO, "r") as archivo:
        lineas = archivo.readlines()[1:]
        for linea in lineas:
            _, nombre, saldo = linea.strip().split(",")
            clientes.append((nombre, float(saldo)))
    
    
    clientes.sort(key=lambda x: x[1])
    
    print("\nClientes ordenados por saldo ascendente:")
    for nombre, saldo in clientes:
        print(f"{nombre}: {saldo}")

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Consultar saldo de un cliente")
        print("2. Contar clientes con saldo > 50")
        print("3. Listar clientes ordenados por saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            contar_mayores_50()
        elif opcion == "3":
            listar_por_saldo()
        elif opcion == "4":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")


menu()