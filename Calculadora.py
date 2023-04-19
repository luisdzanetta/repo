import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
import pandas as pd
from math import sqrt
from scipy.stats import norm

#Original
#def calculate_mde(alpha, beta, cr, control_cr, sample_size, num_variants):
    #pooled_prob = (control_cr + cr * num_variants) / (num_variants)
    #se = sqrt(pooled_prob * (1 - pooled_prob) * ((1 / sample_size) + (num_variants/sample_size)))
    #z_alpha = abs(norm.ppf(alpha/2)) #two-tailed
    ##z_alpha = abs(norm.ppf(alpha)) #one-tailed
    #z_beta = abs(norm.ppf(beta))
    #mde = (z_alpha + z_beta) * se / pooled_prob
    #return mde
    
#Bonferroni     
def calculate_mde(alpha, beta, cr, control_cr, sample_size, num_variants, num_comparisons=1):
    pooled_prob = (control_cr + cr * num_variants) / (num_variants)
    se = sqrt(pooled_prob * (1 - pooled_prob) * ((1 / sample_size) + (num_variants/sample_size)))
    adj_alpha = alpha / num_comparisons
    z_alpha = abs(norm.ppf(adj_alpha/2)) #two-tailed
    #z_alpha = abs(norm.ppf(adj_alpha)) #one-tailed
    z_beta = abs(norm.ppf(beta))
    mde = (z_alpha + z_beta) * se / pooled_prob
    return mde

#Original
#def generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants):
    #table = []
    #mde_values = []
    #total_sample_size_values = []
    #for week in range(1, num_weeks+1):
        #week_total_sample_size = total_sample_size * week
        #week_sample_size = week_total_sample_size / (num_variants)
        #mde = calculate_mde(alpha, beta, control_cr * (1 + 0.01*week), control_cr, week_sample_size, num_variants)
        #mde = calculate_mde(alpha, beta, control_cr, control_cr, week_sample_size, num_variants)
        #week_total_sample_size_str = format(week_total_sample_size, ".0f")
        #week_sample_size_str = format(week_sample_size, ".0f")
        #mde_str = f"{mde*100:.2f}%"
        #table.append([week, week_sample_size_str, week_total_sample_size_str, mde_str])
        #mde_values.append(mde*100)
        #total_sample_size_values.append(week_total_sample_size)
        
#Bonferroni         
def generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants, num_comparisons=1):
    table = []
    mde_values = []
    total_sample_size_values = []
    for week in range(1, num_weeks+1):
        week_total_sample_size = total_sample_size * week
        week_sample_size = week_total_sample_size / (num_variants)
        mde = calculate_mde(alpha, beta, control_cr, control_cr, week_sample_size, num_variants, num_comparisons=num_comparisons)
        week_total_sample_size_str = format(week_total_sample_size, ".0f")
        week_sample_size_str = format(week_sample_size, ".0f")
        mde_str = f"{mde*100:.2f}%"
        table.append([week, week_sample_size_str, week_total_sample_size_str, mde_str])
        mde_values.append(mde*100)
        total_sample_size_values.append(week_total_sample_size)        
         
    sns.set_style("white")
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
       
    fig, ax1 = plt.subplots(figsize=(8,4))
           
    ax1.plot(range(1, num_weeks+1), mde_values, color='#ED1941')
    ax1.set_xlabel('Week')
    ax1.set_ylabel('MDE (%)', color='#ED1941')
    ax1.tick_params('y', colors='#ED1941')
    ax1.set_title("Minimum Detectable Effect vs. Total Sample Size by week", fontsize=10, fontweight='bold', pad=10)
    ax1.set_xlabel('Week', fontsize=8, labelpad=8)
    ax1.set_ylabel('Minimum Detectable Effect (%)', fontsize=8, color='#ED1941', labelpad=10)
    ax1.plot(range(1, num_weeks+1), mde_values, color='#ED1941', linewidth=1.5)
    ax1.tick_params(axis='y', colors='#ED1941', labelsize=5)
    ax1.tick_params(axis='x', labelsize=5)
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=5))
          
    ax2 = ax1.twinx()
    ax2.bar(range(1, num_weeks+1), total_sample_size_values, alpha=0.2, color='#000000')
    ax2.tick_params('y', colors='#000000')
    ax2.set_ylabel('Total Sample Size', fontsize=8, color='#000000', labelpad=10)
    ax2.tick_params(axis='y', colors='#000000', labelsize=5)
    ax2.yaxis.set_major_locator(MaxNLocator(nbins=5))
    ax1.set_zorder(ax2.get_zorder()+1)
    ax1.patch.set_visible(False)
    
    plt.tight_layout()
    
    for i, mde in enumerate(mde_values):
        ax1.annotate(f'{mde:.2f}%', xy=(i+1, mde_values[i]), xytext=(-5, 5), textcoords='offset points', fontsize=7, color='#ED1941')
        #ax2.annotate(f'{total_sample_size_values[i]:,.0f}', xy=(i+1, total_sample_size_values[i]), xytext=(5, -10), textcoords='offset points', fontsize=5, color='#000000')

    headers = ["Week", "Sample Size per variant", "Total Sample Size", "MDE"]
    table_df = pd.DataFrame(table, columns=headers)
    table_styles = [
    dict(selector="th", props=[("border", "1px solid #ccc"), ("background-color", "#f2f2f2"), ("text-align", "center"), ("padding", "8px")]),
    dict(selector="td", props=[("border", "1px solid #ccc"), ("text-align", "center"), ("padding", "8px")]),
    dict(selector=".row-hover:hover", props=[("background-color", "#e2e2e2")]),
    dict(selector="table", props=[("border-collapse", "collapse"), ("box-shadow", "1px 1px 2px #ccc")])
    ]
    
    table_html = table_df.style\
        .set_table_styles(table_styles)\
        .hide_index()\
        .render()
    
    st.markdown(table_html, unsafe_allow_html=True)
    st.divider()
    st.pyplot(fig)
    
st.title("Calculadora de Mínimo Efeito Detectável")
st.write("Este aplicativo calcula o Efeito Mínimo Detectável (MDE) para testes de taxa de conversão com base no nível de significância estatística e poder, número de semanas no experimento, taxa de conversão do controle, tamanho da amostra por semana e número de variantes. Caso você tenha alguma dúvida sobre o cálculo foi feito, visite a página **'Cálculo'**. Para saber mais sobre os conceitos utilizados nesse app, visite a página **'Conceitos e Definições'**.")
alpha = st.slider("Alfa (α)", 0.01, 0.1, 0.05, 0.01)
beta = st.slider("Beta (β)", 0.1, 0.8, 0.2, 0.05)
num_weeks = st.slider("Número de semanas do experimento", 1, 20, 10, 1)
control_cr = st.slider("Conversão do grupo controle (%)", 0.0, 100.0, 5.0, 0.05) / 100
num_variants = st.slider("Número de variantes (incluindo o controle)", 1, 5, 2, 1)
total_sample_size = st.number_input("Amostra por semana", min_value=1, step=100, format="%i")

if st.button("Gerar tabela e gráfico!"):
    generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants)
