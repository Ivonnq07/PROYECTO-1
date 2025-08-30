# Proyecto: Simulador de Presupuesto Mensual

print("======================================")
print("   Simulador de Presupuesto Mensual   ")
print("======================================\n")

# Variables iniciales (se pueden cambiar por input después)
ingresos = 10000  # ingreso mensual
gastos = 0
ahorro = 0
deuda = 2000  # ejemplo de deuda mensual

# Mostrar valores iniciales
print("Ingreso mensual:", ingresos)
print("Deuda mensual:", deuda)

# Simulación básica
gastos = ingresos * 0.50  # 50% a gastos (ejemplo inicial)
ahorro = ingresos * 0.30  # 30% a ahorro
restante = ingresos - gastos - deuda

print("\n--- Resumen ---")
print("Gastos:", gastos)
print("Ahorro:", ahorro)
print("Deuda:", deuda)
print("Dinero restante:", restante)

print("\n(Primer avance: valores fijos de ejemplo)")
