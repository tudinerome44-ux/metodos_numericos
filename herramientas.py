import re

def limpiar_funcion_usuario(entrada):
    #de mayusculas a minusculas y scamos los espacios en blanco de los costados
    entrada = entrada.lower().strip()
    
    entrada = entrada.replace("sen", "sin")
    #estandarizar las potencias
    entrada = entrada.replace("^", "**")
    entrada = re.sub(r'e\*\*\(([^)]+)\)', r'exp(\1)', entrada)
    # También por si ponen la 'e' con exponentes simples sin paréntesis (ej: e**x)
    entrada = entrada.replace("e**x", "exp(x)")
    # Agregamos espacios temporales alrededor de las potencias legítimas (ej: 2**x -> 2 ** x)
    # Esto protege a las bases como el 2 para que no se mezclen con las letras
    entrada = entrada.replace("**", " ** ")
    # Inserta asteriscos si ponen un número pegado a una letra (ej: 2x -> 2*x)
    entrada = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', entrada)
    entrada = entrada.replace(")(", ")*(")
    return entrada

def evaluar_funcion(x,funcion_recibida):
    return(funcion_recibida(x))
