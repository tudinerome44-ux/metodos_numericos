import re

def limpiar_funcion_usuario(entrada):
    entrada = entrada.lower().strip()
    entrada = entrada.replace("sen", "sin")
    entrada = entrada.replace("^", "**")
    entrada = re.sub(r'e\*\*\(([^)]+)\)', r'exp(\1)', entrada)
    entrada = entrada.replace("e**x", "exp(x)")
    entrada = entrada.replace("**", " ** ")
    entrada = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', entrada)
    entrada = entrada.replace(")(", ")*(")
    return entrada

def evaluar_funcion(x,funcion_recibida):
    return(funcion_recibida(x))

def agregar_sugerencias_sidebar():
    import streamlit as st
    st.markdown("""
        <div style="flex-grow: 1; min-height: 10vh;"></div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 💬 Deja tu Sugerencia")
    st.write("¿Encontraste un error o tienes una idea? Ayúdame a mejorar la app.")
    st.page_link(
        "https://forms.gle/mXFjsPMeqaFq1gGq6", 
        label="📝 Abrir Formulario", 
        use_container_width=True
    )