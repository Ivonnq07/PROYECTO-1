# Proyecto: Simulador de Presupuesto Mensual

from typing import get_overloads

def mostrar_bienvenida():
    print("======================================")
    print("   Simulador de Presupuesto Mensual   ")
    print("======================================\n")

def mostrar_valores(ingresos, deuda):
    print("Ingreso mensual:", ingresos)
    print("Deuda mensual:", deuda)


def calcular_presupuesto(ingresos, deuda):
    gastos = ingresos * 0.50 
    ahorro = ingresos * 0.30  
    restante = ingresos - gastos - deuda
    return gastos, ahorro, restante


def mostrar_resumen(gastos, ahorro, deuda, restante):
     print("--- Resumen ---")
     print("Gastos:", gastos)
     print("Ahorro:", ahorro)
     print("Deuda:", deuda)
     print("Dinero restante:", restante)
     if restante > 0:
         print("¡Felicidades! Te sobra dinero este mes.")
     elif restante == 0:
         print("¡Cuidado! No te sobra dinero este mes.")
     else:
         print(" Atencion! Te falta dinero este mes.")

def main():
    mostrar_bienvenida()

    ingresos = float(input("Ingrese su ingreso mensual:"))
    deuda = float(input(" Ingrese su deuda mensual:"))

    mostrar_valores(ingresos, deuda)
    gastos, ahorro, restante = calcular_presupuesto(ingresos, deuda)
    mostrar_resumen(gastos, ahorro, deuda, restante)

if __name__ == "__main__":
    main()