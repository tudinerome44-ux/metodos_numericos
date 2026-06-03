import streamlit as st
from metodos import ejecutar_secante
st.set_page_config(
    page_title="Método de la Secante", 
    page_icon="📐", 
    layout="wide"
)
st.header("Método de la Secante")
st.write("Encuentra raíces de funciones aplicando el metodo de la secante.")

col1_n, col2_n, col3_n = st.columns(3)
with col1_n:
    x0 = st.number_input("Primer punto($x_0$):", value=1.0, step=0.1, key="x0_sec")
    x1 = st.number_input("Segundo punto($x_1$):", value=1.0, step=0.1, key="x1_sec")
with col2_n:
    funcion_secante = st.text_input("Ingrese la función:", value="x**2 - 4", key="fun_sec")     
    r_secante = st.number_input("Error permitido (Tolerancia):", value=0.001, format="%.6f", key="r_sec")
    boton_secante = st.button("CALCULAR SECANTE", type="primary")
with col3_n:
    st.markdown("### 📐 Fórmula de la Secante")
    st.write("La aproximación siguiente se calcula mediante:")
    st.latex(r"x_{n+1} = x_n - \frac{f(x_n) \cdot (x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}")

    
if boton_secante:
    # Newton recibe obligatoriamente 3 parámetros para mantener simetría (exito, resultado, derivada)
    exito, resultado = ejecutar_secante(x0,x1, r_secante, funcion_secante)
    
    if exito:
        num_iter, tabla = resultado
        st.success(f"¡Raíz encontrada con éxito en {num_iter} iteraciones!")
        st.write("### Tabla de iteraciones paso a paso:")
        st.dataframe(
            tabla,
            column_config={
                1: st.column_config.NumberColumn("i", format="%d", alignment="center"),
                2: st.column_config.NumberColumn("xₙ₋₁", format="%.7f", alignment="center"),
                3: st.column_config.NumberColumn("xₙ", format="%.7f", alignment="center"),
                4: st.column_config.NumberColumn("F(xₙ₋₁)", format="%.7f", alignment="center"),
                5: st.column_config.NumberColumn("F(xₙ)", format="%.7f", alignment="center"),
                6: st.column_config.NumberColumn("xₙ₊₁", format="%d", alignment="center"),
                7: st.column_config.NumberColumn("F(xₙ₊₁)", format="%.7f", alignment="center"),
                8: st.column_config.NumberColumn("Error residual", format="%.7f", alignment="center"),
            },
            hide_index=True
        )
    else:
        st.error(f"hubo un problemas: {resultado}")