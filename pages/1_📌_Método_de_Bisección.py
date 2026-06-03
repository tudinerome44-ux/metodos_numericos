import streamlit as st
from metodos import ejecutar_biseccion
st.set_page_config(
    page_title="Método de la Bisección", 
    page_icon="📌", 
    layout="wide"
)

st.header("Método de la Bisección")
st.write("Resuelve tus funciones usando el método de bisección con tablas de iteraciones paso a paso.")

col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("Extremo izquierdo (a):", value=0.0, step=0.1, key="a_bis")
with col2:
    b = st.number_input("Extremo derecho (b):", value=1.0, step=0.1, key="b_bis")
        
with col1:
    r = st.number_input("Error permitido (Tolerancia):", value=0.001, format="%.6f", key="r_bis")
    boton_biseccion = st.button("CALCULAR BISECCIÓN", type="primary")
with col2:
    funcion_biseccion = st.text_input("Ingrese la función:", value="x^2 - 4", key="fun_bis")
        
with col3:
    st.markdown("### 📝 Fórmula del Método")
    st.write("El punto medio $c$ se calcula como:")
    st.latex(r"c = \frac{a + b}{2}")
    st.write("Condición de Bolzano:")
    st.latex(r"f(a) \cdot f(b) < 0")

if boton_biseccion:
    # Bisección recibe exactamente 2 parámetros (exito, resultado)
    exito, resultado = ejecutar_biseccion(a, b, r, funcion_biseccion)
        
    if exito:
        num_iter, tabla = resultado
        st.success(f"¡Raíz encontrada con éxito en {num_iter} iteraciones!")
        st.write("### Tabla de iteraciones paso a paso:")
        st.dataframe(
            tabla,
            column_config={
                #le pongo 8 columnas para que el primero sea el indice
                #los numeros se refieren a las columnas los nombres que aparecen
                1: st.column_config.NumberColumn("i", format="%d", alignment="center"),
                2: st.column_config.NumberColumn("a", format="%.7f", alignment="center"), 
                3: st.column_config.NumberColumn("b", format="%.7f", alignment="center"),
                4: st.column_config.NumberColumn("F(a)", format="%.7f", alignment="center"), 
                5: st.column_config.NumberColumn("F(b)", format="%.7f", alignment="center"),
                6: st.column_config.NumberColumn("c", format="%.7f", alignment="center"),
                7: st.column_config.NumberColumn("F(c)", format="%.7f", alignment="center"),
                8: st.column_config.NumberColumn("Error residual", format="%.7f", alignment="center"),
            },
            hide_index=True
            # Oculta el índice por defecto de Python para que se vea más limpio
        )
    else:
        # Si exito es False
        # muestra el mensaje de error personalizado enviado por el raise u otro error
        st.error(f"hubo un problemas: {resultado}")
