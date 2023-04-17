import streamlit as st

#Equações
st.title("Equações utilizadas")

#Equação MDE
st.markdown(r'''
<div style="text-align: left">
$$\text{MDE} = \frac{(z_{\alpha/2} + z_\beta) \cdot SE}{\text{pooled\_prob}}$$
</div>
''', unsafe_allow_html=True)

st.write('**Onde:**')

#Equação SE
st.markdown(r'''
<div style="text-align: left">
$$\text{SE} = \sqrt{\text{pooled\_prob} \cdot (1 - \text{pooled\_prob}) \cdot \left(\frac{1}{\text{sample\_size}} + \frac{\text{num\_variants}}{\text{sample\_size}}\right)}$$
</div>
''', unsafe_allow_html=True)

#Equação pooled prob
st.markdown(r'''
<div style="text-align: left">
$$\text{pooled\_prob} = \frac{\text{control\_cr} + \text{cr} \cdot \text{num\_variants}}{\text{num\_variants} + 1}$$
</div>
''', unsafe_allow_html=True)

#Equação z de alpha
st.markdown(r'''
<div style="text-align: left">
$$\text{z}_{\alpha/2} = |{\text{norm.ppf}}(\alpha/2)|$$
</div>
''', unsafe_allow_html=True)

#Equação z de beta
st.markdown(r'''
<div style="text-align: left">
$$\text{z}_\beta = |{\text{norm.ppf}}(\beta)|$$
</div>
''', unsafe_allow_html=True)
