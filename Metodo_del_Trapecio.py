import math

def metodo_trapecio():
    """
    Programa que implementa el método del trapecio para integración numérica.
    El usuario puede introducir la función a integrar como una expresión matemática.
    """
    
    print("Método del Trapecio para Integración Numérica")
    print("--------------------------------------------")
    
    # Solicitar la función al usuario
    funcion_str = input("Introduce la función a integrar (usa 'x' como variable, ej: math.sin(x)): ")
    
    # Validar que la función contenga 'x'
    if 'x' not in funcion_str:
        print("Error: La función debe contener la variable 'x'")
        return
    
    # Crear una función lambda a partir del string ingresado
    try:
        funcion = lambda x: eval(funcion_str, {'math': math, 'x': x})
        # Probar la función con un valor cualquiera
        funcion(1.0)
    except:
        print("Error: La función ingresada no es válida")
        return
    
    # Solicitar límites de integración
    try:
        a = float(input("Introduce el límite inferior de integración (a): "))
        b = float(input("Introduce el límite superior de integración (b): "))
    except:
        print("Error: Los límites deben ser valores numéricos")
        return
    
    # Solicitar número de trapecios
    try:
        n = int(input("Introduce el número de trapecios (n): "))
        if n <= 0:
            print("Error: El número de trapecios debe ser positivo")
            return
    except:
        print("Error: El número de trapecios debe ser un entero positivo")
        return
    
    # Calcular el ancho de cada trapecio
    h = (b - a) / n
    
    # Calcular la suma de los extremos
    suma = funcion(a) + funcion(b)
    
    # Calcular la suma de los puntos intermedios
    for i in range(1, n):
        x_i = a + i * h
        suma += 2 * funcion(x_i)
    
    # Calcular la integral aproximada
    integral = (h / 2) * suma
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"Función integrada: f(x) = {funcion_str}")
    print(f"Límites de integración: [{a}, {b}]")
    print(f"Número de trapecios: {n}")
    print(f"Valor aproximado de la integral: {integral:.6f}")

# Ejecutar el programa
if __name__ == "__main__":
    metodo_trapecio()