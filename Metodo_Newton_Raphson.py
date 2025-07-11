import math

def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson para encontrar raíces de funciones.
    
    Args:
        f (function): Función cuya raíz se busca
        f_prime (function): Derivada de la función
        x0 (float): Valor inicial
        tol (float): Tolerancia para la convergencia
        max_iter (int): Número máximo de iteraciones
        
    Returns:
        tuple: (raíz aproximada, número de iteraciones, historial de aproximaciones)
    """
    historial = []
    x_actual = x0
    
    for iteracion in range(max_iter):
        historial.append(x_actual)
        
        try:
            f_val = f(x_actual)
            f_prime_val = f_prime(x_actual)
        except (ValueError, TypeError, ZeroDivisionError) as e:
            raise ValueError(f"Error al evaluar la función o su derivada: {str(e)}")
        
        if abs(f_prime_val) < 1e-10:
            raise ValueError("Derivada cero. El método no puede continuar.")
        
        x_siguiente = x_actual - f_val / f_prime_val
        
        if abs(x_siguiente - x_actual) < tol:
            historial.append(x_siguiente)
            return x_siguiente, iteracion + 1, historial
        
        x_actual = x_siguiente
    
    raise ValueError(f"El método no convergió después de {max_iter} iteraciones")

def parse_function(func_str):
    """
    Convierte un string de función a una función Python ejecutable.
    Permite usar 'x' como variable y funciones de math.
    
    Args:
        func_str (str): String que representa la función (ej. "x**2 - 2")
        
    Returns:
        function: Función Python que puede evaluarse
    """
    # Verificar que la expresión sea segura
    allowed_chars = set("x0123456789.+-*/()^ math.")
    if not all(c in allowed_chars for c in func_str):
        raise ValueError("La función contiene caracteres no permitidos")
    
    # Reemplazar ^ por ** para exponentes
    func_str = func_str.replace('^', '**')
    
    try:
        # Crear la función dinámicamente
        code = f"def f(x):\n    import math\n    return {func_str}"
        locals_dict = {}
        exec(code, {'math': math}, locals_dict)
        return locals_dict['f']
    except Exception as e:
        raise ValueError(f"No se pudo parsear la función: {str(e)}")

def main():
    print("Método de Newton-Raphson para encontrar raíces de funciones")
    print("Ejemplos de funciones válidas:")
    print("- x**2 - 2 (raíz cuadrada de 2)")
    print("- math.exp(x) - 2 (para encontrar ln(2))")
    print("- math.cos(x) - x (solución de cos(x) = x)")
    print("- math.log(x) - 1 (solución de ln(x) = 1)")
    print("\nPara la derivada, ingrese la expresión matemática de la derivada.")
    
    while True:
        try:
            # Entrada de la función y su derivada
            func_str = input("\nIngrese la función (use 'x' como variable, 'math.' para funciones matemáticas): ")
            f = parse_function(func_str)
            
            prime_str = input("Ingrese la derivada de la función: ")
            f_prime = parse_function(prime_str)
            
            # Parámetros del método
            x0 = float(input("Ingrese el valor inicial (x0): "))
            tolerancia = float(input("Ingrese la tolerancia (ej. 1e-6): "))
            max_iter = int(input("Ingrese el máximo de iteraciones: "))
            
            # Ejecutar el método
            raiz, iteraciones, historial = newton_raphson(f, f_prime, x0, tolerancia, max_iter)
            
            # Mostrar resultados
            print(f"\nResultado:")
            print(f"Raíz aproximada: {raiz}")
            print(f"Iteraciones realizadas: {iteraciones}")
            print(f"Valor de la función en la raíz: {f(raiz)}")
            
            # Mostrar historial si no es muy largo
            if len(historial) <= 10:
                print("\nHistorial de aproximaciones:")
                for i, val in enumerate(historial):
                    print(f"Iteración {i}: {val}")
            
        except ValueError as e:
            print(f"\nError: {str(e)}")
        
        continuar = input("\n¿Desea resolver otra función? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()