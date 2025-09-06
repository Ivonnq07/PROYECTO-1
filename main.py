# Proyecto: Simulador de Presupuesto Mensual

def mostrar_bienvenida():
print("======================================")
print("   Simulador de Presupuesto Mensual   ")
print("======================================\n")

def mostrar_valores(ingresos, deuda):
print("Ingreso mensual:", ingresos)
print("Deuda mensual:", deuda)

def calcular_presupuesto(ingresos, deuda):
gastos = ingresos * 0.50  # 50% a gastos (ejemplo inicial)
ahorro = ingresos * 0.30  # 30% a ahorro
restante = ingresos - gastos - deuda
return gastos, ahorro, restante

def mostrar_resumen(gastos, ahorro, deuda, restante):
print("\n--- Resumen ---")
print("Gastos:", gastos)
print("Ahorro:", ahorro)
print("Deuda:", deuda)
print("Dinero restante:", restante)

# Primer avance

def main():
ingresos = 10000
deuda = 2000
mostrar_bienvenida()
mostrar_valores(ingresos, deuda)
gastos, ahorro, restante = calcular_presupuesto(ingresos, deuda)
mostrar_resumen(gastos, ahorro, deuda, restante)

if __name__ == "__main__":
main()
