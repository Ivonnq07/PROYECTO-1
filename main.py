# ======================================================
# Simulador de Presupuesto Mensual
# Autor: Ivonn Quiñónez
# Materia: Pensamiento Computacional para Ingenieria
# Avance 7 - Proyecto Final
# ======================================================
# Incluye funciones, estructuras de decision, ciclos, 
# listas, listas anidadas y librerias externas (random)
# ======================================================

import random # Para generar variaciones aleatorias en los gastos

# -------------------
#    Funciones 
# -------------------

def mostrar_bienvenida():
    """Muestra el titulo del programa."""
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
        porcentaje_gastos = ingresos * 0.50 
        porcentaje_ahorro = ingresos * 0.30 

        # Uso del modulo random: variaciones realistas en los gastos
        variacion = random.uniform(-0.1, 0.1) # entre -10% y +10%
        porcentaje_gastos += (1 + variacion)

         # Estructura de decision: si hay deuda, se paga una parte
        if deuda_restante > 0:
            pago_deuda = min(ingresos * 0.20, deuda_restante)
        else:
            pago_deuda = 0

        deuda_restante -= pago_deuda
        dinero_restante = ingresos - porcentaje_gastos - porcentaje_ahorro - pago_deuda

        # Guardar los datos del mes en una lista (fila)
        datos_mes = [mes, 
                     int(porcentaje_gastos),                         int(porcentaje_ahorro),                         int(pago_deuda),
                     int(deuda_restante), 
                     int(dinero_restante)]

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

        print(f"{mes:>3} | {gastos:>7} | {ahorro:>7} | {pago_deuda:>10}{deuda_restante:>15} | {dinero_restante:>15}")

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

    print(f"\nIngresos mensuales: {int(ingresos)}")
    print(f"Deuda inicial: {int(deuda)}")
    print(f"Meses a simular: {meses}")

    presupuesto_mensual = calcular_presupuesto(ingresos, deuda, meses)

    mostrar_resumen(presupuesto_mensual)

    print("\nGracias por usar el simulador de presupuesto mensual.")


# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    main()