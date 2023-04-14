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
        
    sns.set_style("white")
    sns.color_palette("rocket")
    
    fig = plt.figure(figsize=(10,5))
    #ax1 = fig.add_suplot()
    fig, ax1 = plt.subplots()
    
    ax1.plot(range(1, num_weeks+1), mde_values, color='#ED1941')
    ax1.set_xlabel('Week')
    ax1.set_ylabel('MDE (%)', color='#ED1941')
    ax1.tick_params('y', colors='#ED1941')
    ax1.set_title("Minimum Detectable Effect vs. Total Sample Size", fontsize=10, fontweight='bold', pad=10)
    ax1.set_xlabel('Week', fontsize=8, fontweight='bold', labelpad=10)
    ax1.set_ylabel('Minimum Detectable Effect (%)', fontsize=8, fontweight='bold', color='#ED1941', labelpad=10)
    ax1.plot(range(1, num_weeks+1), mde_values, color='#ED1941', linewidth=2)
    ax1.tick_params(axis='y', colors='#ED1941', labelsize=8)
    ax1.tick_params(axis='x', labelsize=8)
    ax1.grid(alpha=0.3)

    ax2 = ax1.twinx()
    ax2.bar(range(1, num_weeks+1), total_sample_size_values, alpha=1.0, color='#000000')
    ax2.set_ylabel('Total Sample Size', color='#000000')
    ax2.tick_params('y', colors='#000000')
    ax2.set_ylabel('Total Sample Size', fontsize=8, fontweight='bold', color='#000000', labelpad=10)
    ax2.tick_params(axis='y', colors='#000000', labelsize=8)

    plt.tight_layout()

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
    st.pyplot(fig)
st.title("Minimun Detectable Effect (MDE) Calculator")
st.write("This app calculates the Minimum Detectable Effect (MDE) for conversion rate tests based on the level of statistical significance and power, number of weeks in the experiment, conversion rate of the control, sample size per week, and number of variants.")
alpha = st.slider("Statistical significance (α)", 0.01, 0.1, 0.05, 0.01)
beta = st.slider("Statistical power (β)", 0.2, 0.95, 0.8, 0.05)
num_weeks = st.slider("Number of weeks in the experiment", 1, 20, 10, 1)
control_cr = st.slider("Control group conversion rate (%)", 0.0, 100.0, 5.0, 0.05) / 100
num_variants = st.slider("Number of variants (including control)", 1, 6, 2, 1)
total_sample_size = st.number_input("Sample size per week", min_value=0, step=500, format="%i")
if st.button("Generate table and graph"):
    generate_table_and_plot(alpha, beta, num_weeks, control_cr, total_sample_size, num_variants)
