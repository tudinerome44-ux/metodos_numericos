import streamlit as st
from metodos import ejecutar_newton
st.set_page_config(
    page_title="Método de Newton-Raphson", 
    page_icon="⚡", 
    layout="wide"
)
st.header("Método de Newton-Raphson")
st.write("Encuentra raíces de funciones rápidamente usando derivadas analíticas automáticas.")

col1_n, col2_n, col3_n = st.columns(3)
with col1_n:
    x0 = st.number_input("Valor inicial ($x_0$):", value=1.0, step=0.1, key="x0_new")
    st.write("") 
with col2_n:
    r_newton = st.number_input("Error permitido (Tolerancia):", value=0.001, format="%.6f", key="r_new")
    funcion_newton = st.text_input("Ingrese la función:", value="x**2 - 4", key="fun_new")         
    boton_newton = st.button("CALCULAR NEWTON", type="primary")

with col3_n:
    st.markdown("### 📝 Fórmula de Newton")
    st.write("La aproximación siguiente se calcula mediante:")
    st.latex(r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}")
    
if boton_newton:
    # Newton recibe obligatoriamente 3 parámetros para mantener simetría (exito, resultado, derivada)
    exito, resultado, derivada = ejecutar_newton(x0, r_newton, funcion_newton)
    
    if exito:
        num_iter, tabla = resultado
        # Mostramos de forma hermosa la derivada analítica calculada por SymPy
        st.info(f"📐 **Derivada calculada automáticamente:** $${derivada}$$")
        st.success(f"¡Raíz aproximada encontrada en {num_iter} iteraciones!")
        st.write("### Tabla de iteraciones paso a paso:")
        st.dataframe(
            tabla,
            column_config={
                1: st.column_config.NumberColumn("i", format="%d", alignment="center"),
                2: st.column_config.NumberColumn("xn", format="%.7f", alignment="center"),
                3: st.column_config.NumberColumn("F(xn)", format="%.7f", alignment="center"),
                4: st.column_config.NumberColumn("F'(xn)", format="%.7f", alignment="center"),
                5: st.column_config.NumberColumn("Error residual", format="%.7f", alignment="center"),
            },
            hide_index=True
        )
    else:
        # Control seguro: Si hubo un error pero la derivada se llegó a calcular, la mostramos
        if derivada is not None:
            st.info(f"📐 **Derivada calculada automáticamente:** $${derivada}$$")
        # Mostramos el mensaje de error capturado de la excepción (ya sea el personalizado o el inesperado)
        st.error(f"Hubo un problema: {resultado}")