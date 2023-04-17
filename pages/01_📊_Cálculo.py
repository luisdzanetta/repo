import streamlit as st

equacao_mde = r'\text{MDE} = \frac{(z_{\alpha/2} + z_\beta) \cdot SE}{\text{pooled\_prob}}'
equacao_se = r'\text{SE} = \sqrt{\text{pooled\_prob} \cdot (1 - \text{pooled\_prob}) \cdot \left(\frac{1}{\text{sample\_size}} + \frac{\text{num\_variants}}{\text{sample\_size}}\right)}'
equacao_pooled_prob = r'\text{pooled\_prob} = \frac{\text{control\_cr} + \text{cr} \cdot \text{num\_variants}}{\text{num\_variants} + 1}'
equacao_z_alpha_2 = r'\text{z}_{\alpha/2} = \left|\text{norm.ppf}\left(\frac{\alpha}{2}\right)\right|'
equacao_z_beta = r'\text{z}_\beta = \left|\text{norm.ppf}(\beta)\right|'

st.title("Equações utilizadas")
st.write('**Equação MDE:**')
st.markdown(f'<div style="text-align: left">{equacao_mde}</div>', unsafe_allow_html=True)
st.write('**Onde:**')
st.markdown(f'<div style="text-align: left">{equacao_se}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align: left">{equacao_pooled_prob}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align: left">{equacao_z_alpha_2}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align: left">{equacao_z_beta}</div>', unsafe_allow_html=True)
