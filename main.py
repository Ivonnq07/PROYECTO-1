# Proyecto: Simulador de Presupuesto Mensual

def mostrar_bienvenida():
    print("======================================")
    print("   Simulador de Presupuesto Mensual   ")
    print("======================================\n")

def obtener_datos_usuario():
    ingresos = float(input("\nIngrese su ingreso mensual:"))
    deuda = float(input(" Ingrese su deuda inicial:"))
    meses = int(input("¿Cuantos meses quieres simular?:"))
    return ingresos, deuda, meses

def calcular_presupuesto(ingresos, deuda, meses):
    lista_gastos = []
    lista_ahorros = []
    lista_pagos_deuda = []
    lista_deudas_restantes = []
    lista_dinero_restantes = []

    deuda_restante = deuda


    for mes in range(meses):
        porcentaje_gastos= ingresos * 0.50 
        porcentaje_ahorro= ingresos * 0.30  

        if deuda_restante > 0:
            pago_deuda = min(ingresos * 0.20, deuda_restante)
        else:
            pago_deuda = 0

        deuda_restante -= pago_deuda
        dinero_restante = ingresos - porcentaje_gastos - porcentaje_ahorro - pago_deuda

        lista_gastos.append(porcentaje_gastos)
        lista_ahorros.append(porcentaje_ahorro)
        lista_pagos_deuda.append(pago_deuda)
        lista_deudas_restantes.append(deuda)
        lista_dinero_restantes.append(dinero_restante)

    return lista_gastos, lista_ahorros, lista_pagos_deuda, lista_deudas_restantes, lista_dinero_restantes

def mostrar_resumen(meses, lista_gastos, lista_ahorros, lista_pagos_deuda, lista_deudas_restantes, lista_dinero_restantes):
    for i in range(meses):
        print(f"\n---Mes {i+1} ---")
        print(f"Gastos: {lista_gastos[i]:.2f}")
        print(f"Ahorro (reservado): {lista_ahorros[i]:.2f}")
        print(f"Pago deuda: {lista_pagos_deuda[i]:.2f}")
        print(f"Deuda restante: {lista_ahorros[i]:.2f}")
        print(f"Dinero restante (libre despues de todo): {lista_dinero_restantes[i]:.2f}")
    
        if lista_deudas_restantes[i] == 0 and lista_pagos_deuda[i] > 0:
            print("¡Felicidades! Has pagado toda tu deuda.")
        elif lista_dinero_restantes[i] < 0:
            print("¡Atencion! Te falta dinero este mes. ")
        elif lista_dinero_restantes[i] == 0:
            print("¡Cuidado! No te sobro dinero este mes.")

    print("\n--- Resumen Final ---")
    for i in range(meses):
        print(f"Mes {i+1}: Gastos={lista_gastos[i]:.2f},"
              f"Ahorro={lista_ahorros[i]:.2f},"
              f"Pago={lista_pagos_deuda[i]:.2f},"
              f"Deuda={lista_deudas_restantes[i]:.2f},"
              f"Restante={lista_dinero_restantes[i]:.2f}")

def main():
    mostrar_bienvenida()
    ingresos, deuda, meses = obtener_datos_usuario()

    print(f"\nIngresos mensuales: {ingresos}")
    print(f"Deuda inicial: {deuda}")

    lista_gastos, lista_ahorros, lista_pagos_deuda, lista_deudas_restantes, lista_dinero_restantes = calcular_presupuesto(ingresos, deuda, meses)

    mostrar_resumen(meses, lista_gastos, lista_ahorros, lista_pagos_deuda, lista_deudas_restantes, lista_dinero_restantes)

if __name__ == "__main__":
    main()