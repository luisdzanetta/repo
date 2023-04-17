import streamlit as st

st.title("Concepts & Definitions")


st.text_area("Nível de Significância", '''O nível de probabilidade em que se concorda em rejeitar a hipótese nula. 
Conventionalmente estabelecido em 0,05.''')

st.text_area("Alfa (α):", '''A probabilidade do erro tipo I.''')

st.text_area("Erro tipo I", '''O erro que resulta quando a hipótese nula é falsamente rejeitada.''')

st.text_area("Erro tipo II", '''O erro que resulta quando a hipótese nula é falsamente aceita.''')

st.text_area("Hipótese nula", '''Normalmente, a hipótese "sem diferença" ou "sem associação"
              a ser testada (geralmente por meio de um teste de significância)
              contra uma hipótese alternativa que postula diferença ou associação diferente de zero.''')
