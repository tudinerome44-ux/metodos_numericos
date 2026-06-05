import streamlit as st
# --- Configuración global de la página web ---
st.set_page_config(page_title="MÉTODOS NUMÉRICOS", page_icon="🧮", layout="wide")
#layout="wide" se expande el contenido para que pueda ocupar toda la pantalla
st.title("🧮 CALCULADORA DE MÉTODOS NUMÉRICOS")
st.write("Selecciona el método que deseas utilizar en el menú de la izquierda.")
st.markdown("---")

#Desaparecer icono molesto de streamli
st.markdown("""
    <style>
    /* Desaparece el ícono de enlace automático en toda la página */
    .element-container h1 a, .element-container h2 a, .element-container h3 a {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- FILA 1: MÉTODO DE LA BISECCIÓN ---
with st.container():
    st.info("### 📌 Método de la Bisección")
    st.write(
        "Es un algoritmo de búsqueda de raíces que divide el intervalo a la mitad de forma repetitiva "
        "y selecciona un subintervalo en el que radica la raíz para continuar la búsqueda. "
        "Es un método cerrado muy seguro y confiable basado en el Teorema de Bolzano."
    )
    st.page_link("pages/1_📌_Método_de_Bisección.py", label="📟 Abrir Calculadora", use_container_width=True)
    st.caption("👆Haz clic en Abrir calculadora o 👈 deplázate por el menú lateral")

st.write("") # Espacio en blanco para separar las filas

# --- FILA 2: MÉTODO DE NEWTON-RAPHSON ---
with st.container():
    st.info("### ⚡ Método de Newton-Raphson")
    st.write(
        "Es un método abierto que parte de un único valor inicial y utiliza la derivada de la función "
        "para encontrar una aproximación a la raíz en muy pocas iteraciones. "
        "Tiene una velocidad de convergencia cuadrática, lo que lo hace ideal para cálculos rápidos."
    )
    st.page_link("pages/2_⚡_Metódo_de_Newton_Raphson.py", label="📟 Abrir Calculadora", use_container_width=True)
    st.caption("👆Haz clic en Abrir calculadora o 👈 deplázate por el menú lateral")

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
    st.page_link("pages/3_📐_Metódo_de_la_Secante.py", label="📟 Abrir Calculadora", use_container_width=True)
    st.caption("👆Haz clic en Abrir calculadora o 👈 deplázate por el menú lateral")

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
    st.page_link("pages/4_⚖️_Método_de_la_Falsa_Posición.py", label="📟 Abrir Calculadora", use_container_width=True)
    st.caption("👆Haz clic en Abrir calculadora o 👈 deplázate por el menú lateral")

st.markdown("---")
st.caption("Desarrollado con Python y Streamlit.")

with st.sidebar:
    st.write("---")
    st.markdown("### 💬 Deja tu Sugerencia")
    st.write("¿Encontraste un error o tienes una idea? Ayúdame a mejorar la app.")
    
    # Este botón hace la redirección automática hacia tu Google Forms
    st.page_link(
        "https://forms.gle/mXFjsPMeqaFq1gGq6", 
        label="📝 Abrir Formulario", 
        use_container_width=True
    )
