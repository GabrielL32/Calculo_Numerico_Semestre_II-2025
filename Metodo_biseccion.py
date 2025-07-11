import math

def metodo_biseccion(f, a, b, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función f en el intervalo [a, b] usando el método de bisección.
    
    Parámetros:
    f : función
        Función continua para la cual se busca la raíz.
    a, b : float
        Extremos del intervalo [a, b] donde se busca la raíz (debe cumplir f(a)*f(b) < 0).
    tol : float, opcional
        Tolerancia para el criterio de parada (por defecto 1e-6).
    max_iter : int, opcional
        Número máximo de iteraciones (por defecto 100).
    
    Retorna:
    float
        Aproximación de la raíz.
    int
        Número de iteraciones realizadas.
    """
    # Verificar el teorema de Bolzano (condición de cambio de signo)
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")
    
    iteraciones = 0
    c_prev = a  # Valor inicial para la primera comparación
    
    print("\nIteración\t a\t\t b\t\t c\t\t f(c)")
    print("-----------------------------------------------------------")
    
    for iteraciones in range(1, max_iter + 1):
        c = (a + b) / 2  # Punto medio
        f_c = f(c)
        
        print(f"{iteraciones}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f_c:.6f}")
        
        # Criterio de parada: diferencia entre iteraciones o valor de f(c)
        if abs(c - c_prev) < tol or abs(f_c) < tol:
            break
            
        # Actualizar intervalo
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
            
        c_prev = c
    
    return c, iteraciones

def obtener_funcion():
    """
    Permite al usuario ingresar una función matemática como cadena y la convierte en una función callable.
    
    Retorna:
    function
        Función lambda que evalúa la expresión ingresada.
    """
    print("\nIngresa la función f(x) que deseas evaluar.")
    print("Puedes usar operadores matemáticos estándar (+, -, *, /, **)")
    print("y funciones de math (sin, cos, tan, exp, log, sqrt, etc.).")
    print("Ejemplos: x**3 - 2*x - 5, math.sin(x) - x/2, math.exp(-x) - 0.5")
    
    while True:
        try:
            expr = input("\nf(x) = ")
            # Crear una función lambda que evalúa la expresión
            f = lambda x: eval(expr, {'math': math, 'x': x})
            # Probar la función en un valor cualquiera para verificar sintaxis
            f(1.0)
            return f
        except Exception as e:
            print(f"Error en la función ingresada: {e}")
            print("Por favor, ingresa una función válida.")

def obtener_intervalo():
    """
    Solicita al usuario los extremos del intervalo [a, b].
    
    Retorna:
    tuple
        Par (a, b) con los extremos del intervalo.
    """
    while True:
        try:
            a = float(input("\nIngresa el extremo izquierdo del intervalo (a): "))
            b = float(input("Ingresa el extremo derecho del intervalo (b): "))
            if a >= b:
                print("Error: a debe ser menor que b.")
            else:
                return a, b
        except ValueError:
            print("Por favor, ingresa números válidos.")

def obtener_tolerancia():
    """
    Solicita al usuario la tolerancia deseada.
    
    Retorna:
    float
        Valor de la tolerancia.
    """
    while True:
        try:
            tol = float(input("\nIngresa la tolerancia deseada (ej. 0.000001): "))
            if tol <= 0:
                print("La tolerancia debe ser un número positivo.")
            else:
                return tol
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    print("MÉTODO DE BISECCIÓN PARA ENCONTRAR RAÍCES DE FUNCIONES")
    print("------------------------------------------------------")
    
    # Obtener parámetros del usuario
    f = obtener_funcion()
    a, b = obtener_intervalo()
    tol = obtener_tolerancia()
    
    print("\nResolviendo la ecuación ingresada en el intervalo [{}, {}]".format(a, b))
    print("Tolerancia: {}\n".format(tol))
    
    try:
        raiz, iteraciones = metodo_biseccion(f, a, b, tol)
        print("\nResultado:")
        print(f"Raíz aproximada: {raiz:.8f}")
        print(f"Número de iteraciones: {iteraciones}")
        print(f"Valor de f(raíz): {f(raiz):.8f}")
    except ValueError as e:
        print(f"\nError: {e}")
        print("No se puede aplicar el método de bisección porque:")
        print("1. La función no cambia de signo en el intervalo dado, o")
        print("2. La función no es continua en el intervalo dado.")

if __name__ == "__main__":
    main()