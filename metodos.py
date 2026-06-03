from herramientas import evaluar_funcion, limpiar_funcion_usuario
from sympy import sympify, symbols, lambdify

x_simbolo = symbols('x')

def ejecutar_biseccion(a,b,r,funcion_texto):
    try:
        texto_limpio = limpiar_funcion_usuario(funcion_texto)
        expresion_sympy = sympify(texto_limpio)
        f = lambdify(x_simbolo, expresion_sympy, modules ='math')

        lista = [0]*7
        lista[0]  = a
        lista[1] = b
        lista[2] = evaluar_funcion(lista[0],f)
        lista[3] = evaluar_funcion(lista[1],f)
        if (lista[2]*lista[3]>=0):
            raise ValueError("No cumple con el teorema de Bolzano.")
        
        mayor = True
        tabla_iteraciones = []
        num_iteracion = 0
        while(mayor and lista[2]*lista[3]<0):
            num_iteracion +=1
            c = (lista[0]+lista[1])/2
            lista[4] = c
            lista[5] = evaluar_funcion(c,f)
            lista[6] = abs(lista[5])

            #---Guardar el numero de iteracion y la lista----
            fila_atual = [num_iteracion] + list(lista)
            tabla_iteraciones.append(fila_atual)
                    
            if(lista[6]<r):
                mayor=False
                    
            if(lista[2]*lista[5]<0):
                lista[1] = lista[4]
                lista[3] = lista[5]
            else:
                lista[0] = lista[4]
                lista[2] = lista[5]
        return True, (num_iteracion, tabla_iteraciones)
    except ValueError as e:
        return False, str(e)  
    except Exception:
        return False, "Error matemático inesperado al procesar la ecuación en Bisección."



def ejecutar_newton(a,r,funcion_texto):
    try:
        texto_limpio = limpiar_funcion_usuario(funcion_texto)
        expresion_sympy = sympify(texto_limpio)
        derivada_sympy = expresion_sympy.diff(x_simbolo)
        f = lambdify(x_simbolo, expresion_sympy, modules ='math')
        g = lambdify(x_simbolo,derivada_sympy, modules='math')
        lista = [0]*5
        lista[0]  = 0
        lista[1] = a
        lista[2] = evaluar_funcion(lista[1],f)
        derivada_inicial = evaluar_funcion(lista[1],g)
        if derivada_inicial==0:
                raise ValueError("La derivada en el punto inicial es cero. Elija otro punto")
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
    except Exception:
        return False, "Error matemático.", None