import streamlit as st

#Equações
st.title("Equações utilizadas")

#Equação MDE
st.latex(r'''
\text{MDE} = \frac{(z_{\alpha/2} + z_\beta) \cdot SE}{\text{pooled\_prob}}
''')

st.write('**Onde:**')

#Equação SE
st.latex(r'''
\text{SE} = \sqrt{\text{pooled\_prob} \cdot (1 - \text{pooled\_prob}) \cdot \left(\frac{1}{\text{sample\_size}} + \frac{\text{num\_variants}}{\text{sample\_size}}\right)}''')

#Equação pooled prob
st.latex(r'''\text{pooled\_prob} = \frac{\text{control\_cr} + \text{cr} \cdot \text{num\_variants}}{\text{num\_variants} + 1}''')

#Equação z de alpha
st.latex(r'''\text{z}_{\alpha/2} = |{\text{norm.ppf}}(\alpha/2)|''')

#Equação z de beta
st.latex(r'''\text{z}_\beta = |{\text{norm.ppf}}(\beta)|''')
