# 7. Simulación de Colas en Banco:
# Crea un programa que simule el tiempo de espera y de servicio en un banco. 
# El 
# usuario ingresa el número de clientes y el programa calcula el tiempo promedio 
# basado en tiempos de servicio aleatorios.
#  - Referencia de cálculo: Teoría de colas.
from rand import rand
from cola import agregar_clientes
from time import sleep
from number_validation import validar_numero


def main():
    lista_clientes = []
    count = 1
    numero_cliente = input("Ingresa el numero de clientes maximo a atender hoy en el banco: ")
    
    while (validar_numero(numero_cliente)):
         numero_cliente = input("Ingresa el numero CORRECTO  de clientes maximo a atender hoy en el banco: ")
  
    nuevo_numero_cliente = int(numero_cliente)
   
    while(count <= nuevo_numero_cliente):
        tiempo_atencion = rand()
        nombre = "" #input("deme su nombre: ")
        # if len(nombre) == 0:
        #     nombre="no responde"
        print(f"{agregar_clientes(count, nombre)} time: {tiempo_atencion} min")
        lista_clientes.append([agregar_clientes(count, nombre), tiempo_atencion ])
        count += 1
        sleep(0.01)
    
    acumulador = 0
    for elemento in lista_clientes:
       print( elemento)
       acumulador += elemento[1]
    tiempo_promedio = acumulador / nuevo_numero_cliente
    print(acumulador)
    print(f"termina atencion: tiempo promedo de atencion es: {tiempo_promedio}")

main()

