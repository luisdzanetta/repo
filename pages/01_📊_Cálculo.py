import streamlit as st
from scipy.stats import norm

st.title("Cálculo do MDE")

st.write("O **MDE**, é o tamanho mínimo da diferença entre as taxas de conversão das variantes e do grupo de controle que pode ser detectado com um nível de significância alpha e um poder de teste beta. Em outras palavras, se a diferença entre as taxas de conversão das variantes e do grupo de controle for menor que o MDE, não será possível detectar essa diferença com um nível de significância alpha e um poder de teste beta especificados.")

st.write("**Equação para cálculo do MDE**")
st.latex(r'''
\text{MDE} = \frac{(z_{\alpha/2} + z_\beta) \cdot SE}{\text{pooled\_prob}}
''')

st.write("**Onde:**")
         
st.write("**z_alpha/2** é o valor crítico da distribuição normal padrão correspondente ao nível de significância alpha/2. Esse valor é calculado usando a função abs(norm.ppf(alpha/2)). Ele representa a área sob a curva normal à direita de z_alpha/2 para um teste bicaudal com nível de significância alpha.")
st.latex(r'''\text{z}_{\alpha/2} = |{\text{norm.ppf}}(\alpha/2)|''')

st.write("**z_beta** é o valor crítico da distribuição normal padrão correspondente ao poder do teste beta. Esse valor é calculado usando a função abs(norm.ppf(beta)). Ele representa a área sob a curva normal à esquerda de z_beta para um teste bicaudal com poder beta.")
st.latex(r'''\text{z}_\beta = |{\text{norm.ppf}}(\beta)|''')

st.write("**SE** é o erro padrão da diferença entre as taxas de conversão das variantes e do grupo de controle. Ele é calculado usando a fórmula:")
st.latex(r'''
\text{SE} = \sqrt{\text{pooled\_prob} \cdot (1 - \text{pooled\_prob}) \cdot \left(\frac{1}{\text{sample\_size}} + \frac{\text{num\_variants}}{\text{sample\_size}}\right)}''')

st.write("Onde pooled_prob é a taxa de conversão combinada para todas as variantes e o grupo de controle, calculada como:")
st.latex(r'''\text{pooled\_prob} = \frac{\text{control\_cr} + \text{cr} \cdot \text{num\_variants}}{\text{num\_variants}}''')

st.write("E **sample_size** é o tamanho da amostra para cada variante (ou para o grupo de controle, caso num_variants seja maior que 0), ou seja, o número de usuários que serão expostos a cada variante (ou ao grupo de controle) no teste A/B. num_variants é o número de variantes a serem testadas (além do grupo de controle).")

