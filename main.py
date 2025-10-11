# ================================================
# Simulador de Presupuesto Mensual
# Autor: Ivonn Quiñónez
# Materia: Pensamiento Computacional para Ingenieria
# Avance 7 - Proyecto Final
# ================================================

# --- Funciones ---

def mostrar_bienvenida():
    print("======================================")
    print("   Simulador de Presupuesto Mensual   ")
    print("======================================\n")


def obtener_datos_usuario():
    """
    Pide al usuario que ingrese sus ingresos, deuda inicial y meses a simular.
    Devuelve esos valores.
    """
    ingresos = float(input("\nIngrese su ingreso mensual:"))
    deuda = float(input(" Ingrese su deuda inicial:"))
    meses = int(input("¿Cuantos meses quieres simular?:"))
    return ingresos, deuda, meses

def calcular_presupuesto(ingresos, deuda, meses):
    """
    Calcula los gastos; ahorros, pagos de deuda y dinero restante cada mes.
    Devuelve una lista anidada con los datos del presupuesto mensual.
    """
    presupuesto_mensual = []
    deuda_restante = deuda

# Ciclo para siular cada mes
    for mes in range(1, meses + 1):
         # Asignacion de porcentajes
        porcentaje_gastos= ingresos * 0.50 
        porcentaje_ahorro= ingresos * 0.30  

         # Estructura de decision: si hay deuda, se paga una parte
        if deuda_restante > 0:
            pago_deuda = min(ingresos * 0.20, deuda_restante)
        else:
            pago_deuda = 0

        deuda_restante -= pago_deuda
        dinero_restante = ingresos - porcentaje_gastos - porcentaje_ahorro - pago_deuda

        # Guardar los datos del mes en una lista (fila)
        datos_mes = [mes, porcentaje_gastos, porcentaje_ahorro, pago_deuda, deuda_restante, dinero_restante]

        # Agregar la fila a la matriz general
        presupuesto_mensual.append(datos_mes)

    return presupuesto_mensual


def mostrar_resumen(presupuesto_mensual):
    """
    Muestra el resumen del presupuesto mes a mes
    y da mensajes de retroalimentacion segun los resultados.
    """
    print("\n------- Resumen del Presupuesto -------")
    print("Mes | Gastos | Ahorro | Pago Deuda | Deuda Restante | Dinero Restante")
    print("---------------------------------------------------------------------")

        # Ciclo para imprimir cada fila (mes)
    for fila in presupuesto_mensual:
        mes, gastos, ahorro, pago_deuda, deuda_restante, dinero_restante = fila

        print(f"{mes:>3} | {gastos:>7.2f} | {ahorro:>7.2f} | {pago_deuda:>10.2f} | {deuda_restante:>15.2f} | {dinero_restante:>15.2f}")

        # Decisiones condicionales: mensajes personalizados
        if deuda_restante == 0 and pago_deuda > 0:
            print("¡Felicidades! Has pagado toda tu deuda.")
        elif dinero_restante < 0:
            print("¡Atencion! Te falta dinero este mes. ")
        elif dinero_restante == 0:
            print("¡Cuidado! No te sobro dinero este mes.")
        elif dinero_restante > 0:
            print("¡Bien! Te sobro dinero este mes.")
    
# --- Programa Principal ---

def main():
    """
    Funcion principal del programa.
    Llama a las demas funciones para ejecutar todo el proceso.
    """
    mostrar_bienvenida()
    ingresos, deuda, meses = obtener_datos_usuario()

    print(f"\nIngresos mensuales: {ingresos}")
    print(f"Deuda inicial: {deuda}")
    print(f"Meses a siular: {meses}")

    presupuesto_mensual = calcular_presupuesto(ingresos, deuda, meses)

    mostrar_resumen(presupuesto_mensual)

    print("\nGracias por usar el simulador de presupuesto mensual.")


# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    main()