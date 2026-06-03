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
    st.success("### ⚡ Método de Newton-Raphson")
    st.write(
        "Es un método abierto que parte de un único valor inicial y utiliza la derivada de la función "
        "para encontrar una aproximación a la raíz en muy pocas iteraciones. "
        "Tiene una velocidad de convergencia cuadrática, lo que lo hace ideal para cálculos rápidos."
    )
    st.caption("👈 _Haz clic en 'metodo de newton raphson' en el menú lateral para abrir la calculadora._")

st.markdown("---")
st.caption("Desarrollado con Python y Streamlit.")
