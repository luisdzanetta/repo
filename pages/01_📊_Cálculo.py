import streamlit as st

st.title("Equações utilizadas")

with st.beta_container():
    st.markdown("""
        <div style="text-align: left">
        
        $$\text{MDE} = \frac{(z_{\\alpha/2} + z_\\beta) \\cdot \\text{SE}}{\\text{pooled_prob}}$$
        
        </div>
    """, unsafe_allow_html=True)

with st.beta_container():
    st.markdown("""
        <div style="text-align: left">
        
        **Onde:**

        $$\\text{SE} = \\sqrt{\\text{pooled_prob} \\cdot (1 - \\text{pooled_prob}) \\cdot \\left(\\frac{1}{\\text{sample_size}} + \\frac{\\text{num_variants}}{\\text{sample_size}}\\right)}$$

        $$\\text{pooled_prob} = \\frac{\\text{control_cr} + \\text{cr} \\cdot \\text{num_variants}}{\\text{num_variants} + 1}$$

        $$\\text{z}_{\\alpha/2} = |{\\text{norm.ppf}}(\\alpha/2)|$$

        $$\\text{z}_\\beta = |{\\text{norm.ppf}}(\\beta)|$$
        
        </div>
    """, unsafe_allow_html=True)
