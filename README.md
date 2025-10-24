# Simulador de Presupuesto Mensual

### Contexto
La administraciòn del dinero es una habilidad esencial en la vida diaria. Muchas veces los estudiantes no saben còmo distribuir sus ingresos de manera eficiente, lo que puede llevar a gastar màs de lo que se gana o a no ahorrar lo suficiente.

Este proyecto propone un simulador de presupuesto mensual que permite organizar los ingresos de forma sencilla, distribuyèndolos en categorìas como necesidades, deseos y ahorro, basàndose en la conocida regla del 50-30-20.

Lo interesante es que el usuario no solo podrà ajustar los porcentajes de distribuciòn a su gusto, sino tambièn agregar deudas mensuales, lo cual hace que el simulador se acerque màs a situaciones reales de la vida cotidiana.

### Algoritmo

1. Iniciar el programa y mostrar un mensaje de bienvenida.
2. Solicitar al usuario los siguientes datos:
   • Ingreso mensual.
   • Monto total de deuda.
   • Número de meses a simular.
3. Inicializar una lista vacía llamada presupuesto_mensual para almacenar los datos de cada mes.
4. Asignar la variable deuda_restante con el valor inicial de la deuda.
5. Para cada mes (uso de ciclo for):
   5.1. Calcular los gastos (50% del ingreso).
   5.2. Calcular el ahorro (30% del ingreso).
   5.3. Si la deuda aún no está pagada, calcular el pago de deuda (20% o el total restante si es menor).
   5.4. Restar el pago de deuda de la deuda restante.
   5.5. Calcular el dinero restante del mes (ingreso – gastos – ahorro – pago de deuda).
   5.6. Guardar los valores del mes (mes, gastos, ahorro, pago de deuda, deuda restante, dinero restante) en una lista.
   5.7. Agregar esa lista como una fila dentro de la lista principal presupuesto_mensual (creando una matriz).
6. Mostrar en pantalla una tabla con los resultados de cada mes, incluyendo:
   • Mes, gastos, ahorro, pago de deuda, deuda restante y dinero restante.
7. Evaluar los resultados de cada mes mediante condiciones (if):
   • Si la deuda llega a cero, mostrar mensaje de felicitación.
   • Si el dinero restante es negativo, mostrar advertencia.
   • Si el dinero restante es positivo o cero, mostrar retroalimentación correspondiente.
8. Finalizar el programa mostrando un mensaje de despedida.

### Instrucciones

Descargar el archivo y correr en terminal con:


    main.py
    
o abrir en Replit y dar boton de Run project.

Responder a las preguntas que aparecen, el programa tiene instrucciones y no usa bibliotecas no standard.

gracias por visitar
