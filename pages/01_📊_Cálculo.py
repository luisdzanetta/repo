import streamlit as st

st.title("Cálculo utilizado")

st.latex(r'''
\text{MDE} = \frac{(z_{\alpha/2} + z_\beta) \cdot SE}{\text{pooled\_prob}}
''')

st.latex(r'''
\begin{aligned}
SE &= \sqrt{\text{pooled\_prob} \cdot (1 - \text{pooled\_prob}) \cdot \left(\frac{1}{\text{sample\_size}} + \frac{\text{num\_variants}}{\text{sample\_size}}\right)} \\
\text{pooled\_prob} &= \frac{\text{control\_cr} + \text{cr} \cdot \text{num\_variants}}{\text{num\_variants} + 1} \\
z_{\alpha/2} &= |\text{norm.ppf}(\alpha/2)| \\
z_\beta &= |\text{norm.ppf}(\beta)|
\end{aligned}
''')
