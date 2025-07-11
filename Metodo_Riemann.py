import math

def calcular_integral_riemann():
    """
    Calcula la integral definida de una función usando el método de Riemann.
    El usuario ingresa la función, los límites de integración y el número de subintervalos.
    """
    
    print("Calculadora de Integrales usando el método de Riemann")
    print("----------------------------------------------------")
    
    # Solicitar la función al usuario
    while True:
        try:
            funcion_str = input("Ingrese la función a integrar (use 'x' como variable, ej: x**2 + math.sin(x)): ")
            # Probamos la función con un valor de prueba para ver si es válida
            x = 1
            eval(funcion_str)
            break
        except Exception as e:
            print(f"Error en la función ingresada: {e}. Intente nuevamente.")
    
    # Solicitar límites de integración
    while True:
        try:
            a = float(input("Ingrese el límite inferior de integración (a): "))
            b = float(input("Ingrese el límite superior de integración (b): "))
            if b < a:
                print("El límite superior debe ser mayor que el inferior. Se intercambiarán los valores.")
                a, b = b, a
            break
        except ValueError:
            print("Por favor ingrese números válidos.")
    
    # Solicitar número de subintervalos
    while True:
        try:
            n = int(input("Ingrese el número de subintervalos (n): "))
            if n <= 0:
                print("El número de subintervalos debe ser positivo.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número entero válido.")
    
    # Calcular el ancho de cada subintervalo
    delta_x = (b - a) / n
    
    # Inicializar la suma
    suma = 0.0
    
    # Método de Riemann (punto derecho)
    for i in range(1, n+1):
        x_i = a + i * delta_x
        try:
            # Evaluar la función en x_i
            y_i = eval(funcion_str, {'math': math, 'x': x_i})
            suma += y_i * delta_x
        except Exception as e:
            print(f"Error al evaluar la función en x = {x_i}: {e}")
            return
    
    # Mostrar el resultado
    print("\nResultado:")
    print(f"La integral aproximada de {funcion_str} desde {a} hasta {b} es: {suma}")
    
    # Opción para mostrar más detalles
    detalle = input("\n¿Desea ver detalles del cálculo? (s/n): ").lower()
    if detalle == 's':
        print(f"\nDetalles del cálculo:")
        print(f"- Método usado: Sumas de Riemann (punto derecho)")
        print(f"- Número de subintervalos: {n}")
        print(f"- Ancho de cada subintervalo (Δx): {delta_x}")
        print(f"- Suma total: {suma}")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_integral_riemann()
    
    # Preguntar si desea calcular otra integral
    while True:
        continuar = input("\n¿Desea calcular otra integral? (s/n): ").lower()
        if continuar == 'n':
            print("¡Hasta luego!")
            break
        elif continuar == 's':
            calcular_integral_riemann()
        else:
            print("Opción no válida. Por favor ingrese 's' o 'n'.")