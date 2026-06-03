from herramientas import evaluar_funcion, limpiar_funcion_usuario
from sympy import sympify, symbols, lambdify

x_simbolo = symbols('x')

def ejecutar_biseccion(a,b,r,funcion_texto):
    try:
        texto_limpio = limpiar_funcion_usuario(funcion_texto)
        expresion_sympy = sympify(texto_limpio)
        f = lambdify(x_simbolo, expresion_sympy, modules ='math')
        fa = evaluar_funcion(a,f)
        fb = evaluar_funcion(b,f)

        if (fa*fb>=0):
            raise ValueError("No cumple con el teorema de Bolzano.")

        lista = [0]*8
        lista[0]  = 1
        lista[1] = a
        lista[2] = b
        lista[3] = evaluar_funcion(lista[1],f)
        lista[4] = evaluar_funcion(lista[2],f)
        lista[5] = (lista[1]+lista[2])/2
        lista[6] = evaluar_funcion(lista[5],f)
        lista[7] = abs(lista[6])
        tabla_iteraciones = []
        while(lista[7]>=r):
            tabla_iteraciones.append(list(lista))
            lista[0]  += 1
            if(lista[3]*lista[6]<0):
                lista[2] = lista[5]
                lista[4] = lista[6]
            else:
                lista[1] = lista[5]
                lista[3] = lista[6]

            lista[5] = (lista[1]+lista[2])/2
            lista[6] = evaluar_funcion(lista[5],f)
            lista[7] = abs(lista[6])

        tabla_iteraciones.append(list(lista))
        return True, (lista[0], tabla_iteraciones)
    except ValueError as e:
        return False, str(e)
    except ZeroDivisionError:
        return False, "Error matemático: La función no está definida en uno de los puntos evaluados (división por cero)."
    except Exception:
        return False, "Error matemático inesperado al procesar la ecuación en Bisección."

def ejecutar_newton(a,r,funcion_texto):
    try:
        texto_limpio = limpiar_funcion_usuario(funcion_texto)
        expresion_sympy = sympify(texto_limpio)
        derivada_sympy = expresion_sympy.diff(x_simbolo)
        f = lambdify(x_simbolo, expresion_sympy, modules ='math')
        g = lambdify(x_simbolo,derivada_sympy, modules='math')
        derivada_inicial = evaluar_funcion(a,g)
        if derivada_inicial==0:
            raise ValueError("La derivada en el punto inicial es cero. Elija otro punto")
        
        lista = [0]*5
        lista[0]  = 0
        lista[1] = a
        lista[2] = evaluar_funcion(lista[1],f)
        lista[3] =derivada_inicial
        lista[4] = abs(lista[2])
        tabla_iteraciones=[]
        while(lista[4]>=r and lista[0]<50):
            tabla_iteraciones.append(list(lista))
            
            proximo = lista[1]-(lista[2])/lista[3]
            derivada_i = evaluar_funcion(proximo,g)
            if derivada_i==0:
                raise ValueError(f"La derivada se hizo cero en la iteración {lista[0]+1} (punto {proximo:.4f})")
            
            lista[0] +=1
            lista[1] = proximo
            lista[2] = evaluar_funcion(lista[1],f)
            lista[3] = derivada_i
            lista[4] = abs(lista[2])

        tabla_iteraciones.append(list(lista))

        return True, (lista[0], tabla_iteraciones), derivada_sympy
    except ValueError as e:
        return False, str(e), derivada_sympy  
    except ZeroDivisionError:
        return False, "Error matemático: (división por cero).", None
    except Exception:
        return False, "Error matemático.", None

def ejecutar_secante(x0,x1,r,funcion_texto):
    try:
        texto_limpio = limpiar_funcion_usuario(funcion_texto)
        expresion_sympy = sympify(texto_limpio)
        f = lambdify(x_simbolo, expresion_sympy, modules ='math')
        
        f0 = evaluar_funcion(x0,f)
        f1 = evaluar_funcion(x1,f)
        if (f1 - f0)==0:
            raise ValueError(f"Error: (división por cero). f({x1}) y f({x0}) son iguales.")
        lista = [0]*8
        lista[0]  = 1
        lista[1] = x0
        lista[2] = x1
        lista[3] = f0
        lista[4] = f1
        lista[5] = lista[2] - (lista[4]*(lista[2] - lista[1]))/(lista[4] - lista[3])
        lista[6] = evaluar_funcion(lista[5],f)
        lista[7] = abs(lista[6])
        tabla_iteraciones=[]
        while(lista[7]>=r):
            tabla_iteraciones.append(list(lista))
            lista[0]  += 1
            lista[1] = lista[2]
            lista[2] = lista[5]
            lista[3] = lista[4]
            lista[4] = lista[6]
            if (lista[4] - lista[3])==0:
                raise ValueError(f"Error: (división por cero). f({lista[4]}) y f({lista[3]}) son iguales.")
            
            lista[5] = lista[2] - (lista[4]*(lista[2] - lista[1]))/(lista[4] - lista[3])
            lista[6] = evaluar_funcion(lista[5],f)
            lista[7] = abs(lista[6])

        tabla_iteraciones.append(list(lista))
        return True, (lista[0], tabla_iteraciones)

    except ValueError as e:
        return False, str(e)
    except ZeroDivisionError:
        return False, "Error matemático: La función no está definida en uno de los puntos evaluados (división por cero)."
    except Exception:
        return False, "Error matemático al procesar la ecuacion con el metodo de la secante."
    
def ejecutar_falsa_posicion(a,b,r,funcion_texto):
    try:
        texto_limpio = limpiar_funcion_usuario(funcion_texto)
        expresion_sympy = sympify(texto_limpio)
        f = lambdify(x_simbolo, expresion_sympy, modules ='math')
        fa = evaluar_funcion(a,f)
        fb = evaluar_funcion(b,f)
        if (fa*fb>=0):
            raise ValueError("No cumple con el teorema de Bolzano.")
        if (fb - fa)==0:
            raise ValueError(f"Division por cero. f({a}) y f({b}) son iguales. \nNo se puede hallar el valor aproximado de la raíz.")
        
        lista = [0]*8
        lista[0]  = 1
        lista[1] = a
        lista[2] = b
        lista[3] = fa
        lista[4] = fb
        lista[5] = lista[2] - (lista[4]*(lista[2] - lista[1]))/(lista[4] - lista[3])
        lista[6] = evaluar_funcion(lista[5],f)
        lista[7] = abs(lista[6])
        tabla_iteraciones=[]
        while(lista[7]>=r):
            tabla_iteraciones.append(list(lista))
            
            lista[0]  += 1
            if(lista[3]*lista[6]<0):
                lista[2] = lista[5]
                lista[4] = lista[6]
            else:
                lista[1] = lista[5]
                lista[3] = lista[6]
            if (lista[4] - lista[3])==0:
                raise ValueError(f"Division por cero. f({lista[2]}) y f({lista[1]}) son iguales. \nNo se puede hallar el valor aproximado de la raíz.")
        
            lista[5] = lista[2] - (lista[4]*(lista[2] - lista[1]))/(lista[4] - lista[3])
            lista[6] = evaluar_funcion(lista[5],f)
            lista[7] = abs(lista[6])

        tabla_iteraciones.append(list(lista))
        return True, (lista[0], tabla_iteraciones)

    except ValueError as e:
        return False, str(e)
    except ZeroDivisionError:
        return False, "Error matemático: La función no está definida en uno de los puntos evaluados (división por cero)."
    except Exception:
        return False, "Error matemático al procesar la ecuacion con el metodo de la falsa posición."
    
