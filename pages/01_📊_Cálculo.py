import streamlit as st

#Equações
st.title("Equações utilizadas")

#Equação MDE
st.write(f'<div style="text-align: left">{r"$$\text{{MDE}} = \\\\frac{{(z_{{\\\\alpha/2}} + z_\\\\beta) \\\\cdot \\\\text{{SE}}}}{{\\\\text{{pooled\_prob}}}}$$"}</div>', unsafe_allow_html=True)

st.write('**Onde:**')

#Equação SE
st.write(f'<div style="text-align: left">{r"$$\text{{SE}} = \\sqrt{{\\text{{pooled\_prob}} \\cdot (1 - \\text{{pooled\_prob}}) \\cdot \\left(\\frac{{1}}{{\\text{{sample\_size}}}} + \\frac{{\\text{{num\_variants}}}}{{\\text{{sample\_size}}}}\\right)}}$$"}</div>', unsafe_allow_html=True)

#Equação pooled prob
st.write(f'<div style="text-align: left">{r"$$\\text{{pooled\_prob}} = \\frac{{\\text{{control\_cr}} + \\text{{cr}} \\cdot \\text{{num\_variants}}}}{{\\text{{num\_variants}} + 1}}$$"}</div>', unsafe_allow_html=True)

#Equação z de alpha
st.write(f'<div style="text-align: left">{r"$$z_{{\\alpha/2}} = |{{\\text{{norm.ppf}}(\\alpha/2)}}|$$"}</div>', unsafe_allow_html=True)

#Equação z de beta
st.write(f'<div style="text-align: left">{r"$$z_\\beta = |{{\\text{{norm.ppf}}(\\beta)}}|$$"}</div>', unsafe_allow_html=True)

