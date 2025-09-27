# Proyecto: Simulador de Presupuesto Mensual

def mostrar_bienvenida():
    print("======================================")
    print("   Simulador de Presupuesto Mensual   ")
    print("======================================\n")

def mostrar_valores(ingresos, deuda):
    print("Ingreso mensual:", ingresos)
    print("Deuda inicial:", deuda)


def calcular_presupuesto(ingresos, deuda):
    gastos = ingresos * 0.50 
    ahorro = ingresos * 0.30  
    disponible = ingresos - gastos
    pago_max = ingresos * 0.20
    pago_deuda = min(disponible, deuda, pago_max)
    deuda_restante = deuda - pago_deuda
    restante = disponible - pago_deuda
    return gastos, ahorro, deuda_restante, restante


def mostrar_resumen(mes, gastos, ahorro, deuda, restante):
     print(f"\n--- Mes {mes} ---")
     print("Gastos:", gastos)
     print("Ahorro:", ahorro)
     print("Deuda restante:", deuda)
     print("Dinero restante:", restante)
     if restante > 0:
         print("¡Felicidades! Te sobra dinero este mes.")
     elif restante == 0:
         print("¡Cuidado! No te sobra dinero este mes.")
     else:
         print(" Atencion! Te falta dinero este mes.")

def main():
    mostrar_bienvenida()

    ingresos = float(input("\nIngrese su ingreso mensual:"))
    deuda = float(input(" Ingrese su deuda inicial:"))
    meses = int(input("¿Cuantos meses quieres simular?:"))

    mostrar_valores(ingresos, deuda)

    for mes in range(1, meses + 1):
        gastos, ahorro, deuda, restante = calcular_presupuesto(ingresos, deuda)
        mostrar_resumen(mes, gastos, ahorro, deuda, restante)

    print("\n Fin de la simulacion.")


if __name__ == "__main__":
    main()