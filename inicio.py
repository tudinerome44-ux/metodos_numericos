import streamlit as st
# --- Configuración global de la página web ---
st.set_page_config(page_title="MÉTODOS NUMÉRICOS", page_icon="🧮", layout="wide")
#layout="wide" se expande el contenido para que pueda ocupar toda la pantalla
st.title("🧮 CALCULADORA DE MÉTODOS NUMÉRICOS")
st.write("Selecciona el método que deseas utilizar en el menú de la izquierda.")
st.markdown("---")

# --- FILA 1: MÉTODO DE LA BISECCIÓN ---
with st.container():
    st.info("### 📌 Método de la Bisección")
    st.write(
        "Es un algoritmo de búsqueda de raíces que divide el intervalo a la mitad de forma repetitiva "
        "y selecciona un subintervalo en el que radica la raíz para continuar la búsqueda. "
        "Es un método cerrado muy seguro y confiable basado en el Teorema de Bolzano."
    )
    st.caption("👈 _Haz clic en 'metodo de biseccion' en el menú lateral para abrir la calculadora._")

st.write("") # Espacio en blanco para separar las filas

# --- FILA 2: MÉTODO DE NEWTON-RAPHSON ---
with st.container():
    st.info("### ⚡ Método de Newton-Raphson")
    st.write(
        "Es un método abierto que parte de un único valor inicial y utiliza la derivada de la función "
        "para encontrar una aproximación a la raíz en muy pocas iteraciones. "
        "Tiene una velocidad de convergencia cuadrática, lo que lo hace ideal para cálculos rápidos."
    )
    st.caption("👈 _Haz clic en 'metodo de newton raphson' en el menú lateral para abrir la calculadora._")

st.write("") 

# --- FILA 3: MÉTODO DE LA SECANTE ---
with st.container():
    st.info("### 📐 Método de la Secante")
    st.write(
        "Es un método abierto que parte de dos valores iniciales y utiliza una línea recta "
        "que corta a la curva (recta secante) para aproximar el punto donde la función cruza el eje x. "
        "Tiene una velocidad de convergencia superlineal, siendo la mejor opción cuando "
        "no se conoce o es muy difícil evaluar la función de la derivada."
    )
    st.caption("👈 _Haz clic en 'metodo de la secante' en el menú lateral para abrir la calculadora._")

st.write("") 

# --- FILA 4: MÉTODO DE LA FALSA POSICION ---
with st.container():
    st.info("### ⚖️ Método de la Falsa Posición")
    st.write(
        "Es un método cerrado que encierra la raíz en un intervalo mediante el teorema de Bolzano. "
        "Calcula la aproximación trazando una línea recta entre los extremos para acelerar la búsqueda. "
        "Combina la seguridad de la bisección con el cálculo geométrico de la secante. "
        "Es ideal cuando se busca convergencia garantizada con mayor eficiencia que el corte a la mitad."
    )

    st.caption("👈 _Haz clic en 'metodo de la falsa poscion ' en el menú lateral para abrir la calculadora._")

st.markdown("---")
st.caption("Desarrollado con Python y Streamlit.")
