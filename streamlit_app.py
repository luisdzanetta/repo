pip install -q streamlit
pip install matplotlib
pip install seaborn
pip install pandas
pip install math
pip install scipy

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from math import sqrt
from scipy.stats import norm

def calculate_mde(alpha, beta, cr, control_cr, sample_size, num_variants):
    pooled_prob = (control_cr + cr * num_variants) / (num_variants + 1)
    se = sqrt(pooled_prob * (1 - pooled_prob) * (1/sample_size + num_variants/sample_size))
    z_alpha = abs(norm.ppf(alpha/2))
    z_beta = abs(norm.ppf(beta))
    mde = (z_alpha + z_beta) * se / pooled_prob
    return mde

def generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants):
    table = []
    mde_values = []
    total_sample_size_values = []
    for week in range(1, num_weeks+1):
        week_total_sample_size = total_sample_size * week
        week_sample_size = week_total_sample_size / (num_variants)
        mde = calculate_mde(alpha, beta, control_cr * (1 + 0.01*week), control_cr, week_sample_size, num_variants) * 100
        week_total_sample_size_str = format(week_total_sample_size, ".0f")
        week_sample_size_str = format(week_sample_size, ".0f")
        mde_str = f"{mde:.2f}%"
        table.append([week, week_sample_size_str, week_total_sample_size_str, mde_str])
        mde_values.append(mde)
        total_sample_size_values.append(week_total_sample_size)

    sns.set_style("whitegrid")
    fig, ax1 = plt.subplots()
    ax1.plot(range(1, num_weeks+1), mde_values, 'b-')
    ax1.set_xlabel('Week')
    ax1.set_ylabel('MDE (%)', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.bar(range(1, num_weeks+1), total_sample_size_values, alpha=0.2, color='g')
    ax2.set_ylabel('Total Sample Size', color='g')
    ax2.tick_params('y', colors='g')

    headers = ["Week", "Sample Size per variant", "Total Sample Size", "MDE"]
    table_df = pd.DataFrame(table, columns=headers)
    st.table(table_df)

    st.pyplot(fig)

st.title("Calculadora de Tamanho de Amostra para Testes A/B")
st.write("Este app calcula o tamanho de amostra necessário para um teste A/B com um número de variantes e número de semanas especificados. O tamanho de amostra é calculado com base em um nível de significância, poder estatístico, taxa de conversão do grupo de controle e tamanho total da amostra. O resultado é apresentado em uma tabela e um gráfico.")

alpha = st.slider("Nível de significância (alfa)", 0.01, 0.1, 0.05, 0.01)
beta = st.slider("Poder estatístico (beta)", 0.01, 0.3, 0.2, 0.05)
num_weeks = st.slider("Número de semanas", 1, 20, 10, 1)
control_cr = st.slider("Taxa de conversão do grupo de controle (%)", 0.0, 100.0, 5.0, 0.05) / 100
total_sample_size = st.slider("Tamanho total da amostra", 1000, 1000000, 500000, 1000)
num_variants = st.slider("Número de variantes", 1, 6, 2, 1)

if st.button("Gerar tabela e gráfico"):
    generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants)
