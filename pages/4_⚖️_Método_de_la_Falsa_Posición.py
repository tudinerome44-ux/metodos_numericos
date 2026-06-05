import streamlit as st
from metodos import ejecutar_falsa_posicion
from herramientas import agregar_sugerencias_sidebar as sugerencia
st.set_page_config(
    page_title="Método de la Falsa Posición", 
    page_icon="⚖️", 
    layout="wide"
)

st.header("Método de la Falsa Posición")
st.write("Resuelve tus funciones usando el método de la falsa posición con tablas de iteraciones paso a paso.")

col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("Extremo izquierdo (a):", value=0.0, step=0.1, key="a_falp")
    b = st.number_input("Extremo derecho (b):", value=1.0, step=0.1, key="b_falp")
with col2:
    r = st.number_input("Error permitido (Tolerancia):", value=0.001, format="%.6f", key="r_falp")
    funcion_falsa_posicion = st.text_input("Ingrese la función:", value="x^2 - 4", key="fun_falp")
    boton_falsa_posicion = st.button("CALCULAR FALSA POSICIÓN", type="primary")
      
with col3:
    st.markdown("### 📐 Fórmula del Método")
    st.write("Condición de Bolzano:")
    st.latex(r"f(a) \cdot f(b) < 0")
    st.write("La aproximación siguiente se calcula mediante:")
    st.latex(r"x_r = b - \frac{f(b) \cdot (b - a)}{f(b) - f(a)}")
    

if boton_falsa_posicion:
    exito, resultado = ejecutar_falsa_posicion(a, b, r, funcion_falsa_posicion)
        
    if exito:
        num_iter, tabla = resultado
        st.success(f"¡Raíz encontrada con éxito en {num_iter} iteraciones!")
        st.write("### Tabla de iteraciones paso a paso:")
        st.dataframe(
            tabla,
            column_config={
                1: st.column_config.NumberColumn("i", format="%d", alignment="center"),
                2: st.column_config.NumberColumn("a", format="%.7f", alignment="center"), 
                3: st.column_config.NumberColumn("b", format="%.7f", alignment="center"),
                4: st.column_config.NumberColumn("F(a)", format="%.7f", alignment="center"), 
                5: st.column_config.NumberColumn("F(b)", format="%.7f", alignment="center"),
                6: st.column_config.NumberColumn("xᵣ", format="%.7f", alignment="center"),
                7: st.column_config.NumberColumn("F(xᵣ)", format="%.7f", alignment="center"),
                8: st.column_config.NumberColumn("Error residual", format="%.7f", alignment="center"),
            },
            hide_index=True
        )
    else:
        st.error(f"hubo un problemas: {resultado}")


with st.sidebar:
    sugerencia()