import streamlit as st
import matplotlib
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

    # define a paleta de cores
colors = ['#ED1941', '#F26522', '#F7B32B', '#00A8E0', '#00CCBC']

# cria o gráfico
sns.set_style("whitegrid")
fig, ax1 = plt.subplots(figsize=(10,6))

# define as propriedades do eixo x
ax1.set_xlabel('Week', fontsize=12, fontweight='bold', labelpad=10)
ax1.set_xticks(range(1, num_weeks+1))
ax1.tick_params(axis='x', labelsize=10)

# define as propriedades do eixo y1
ax1.set_ylabel('Minimum Detectable Effect (%)', fontsize=12, fontweight='bold', color=colors[0], labelpad=10)
ax1.plot(range(1, num_weeks+1), mde_values, color=colors[0], linewidth=2, marker='o', markersize=8)
ax1.tick_params(axis='y', colors=colors[0], labelsize=10)

# define as propriedades do eixo y2
ax2 = ax1.twinx()
ax2.bar(range(1, num_weeks+1), total_sample_size_values, alpha=0.2, color=colors[-1])
ax2.set_ylabel('Total Sample Size', fontsize=12, fontweight='bold', color=colors[-1], labelpad=10)
ax2.tick_params(axis='y', colors=colors[-1], labelsize=10)

# adiciona linhas de grade horizontais para ambos os eixos
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# ajusta o layout do gráfico
plt.tight_layout()

# exibe o gráfico
st.pyplot(fig)

st.title("Minimun Detectable Effect (MDE) Calculator")
st.write("This app calculates the Minimum Detectable Effect (MDE) for conversion rate tests based on the level of statistical significance and power, number of weeks in the experiment, conversion rate of the control, sample size per week, and number of variants.")

alpha = st.slider("Statistical significance (α)", 0.01, 0.1, 0.05, 0.01)
beta = st.slider("Statistical power (β)", 0.2, 0.95, 0.8, 0.05)
num_weeks = st.slider("Number of weeks in the experiment", 1, 20, 10, 1)
control_cr = st.slider("Control group conversion rate (%)", 0.0, 100.0, 5.0, 0.05) / 100
total_sample_size = st.slider("Sample size per week", 1000, 1000000, 500000, 1000)
num_variants = st.slider("Number of variants (including control)", 1, 6, 2, 1)

if st.button("Generate table and graph"):
    generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants)
