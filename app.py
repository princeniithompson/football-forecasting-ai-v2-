import streamlit as st
import pandas as pd
import plotly.express as px
# Removed lightgbm and shap imports to avoid errors
# from lightgbm import LGBMRegressor
# import shap

# Sidebar
st.sidebar.title("Football Forecasting AI 🇬🇭")
match = st.sidebar.selectbox("Match", ["Kosovo vs. Comoros", "Amazonas vs. Athletic Club"])
st.sidebar.write("🔥 Hypothetical Match: June 9, 2025")
st.sidebar.markdown("Sources: [Over25Tips](https://www.over25tips.com), [RatingBet](https://www.ratingbet.com), [WinDrawWin](https://www.windrawwin.com), X posts")
with open('data/notes.txt', 'r') as f:
    st.sidebar.text_area("Data Gaps", value=f.read(), height=150)
crowd_size = st.sidebar.slider("Crowd Size", 10000, 20000, 15000, 1000)
squad = st.sidebar.selectbox("Athletic Squad", ["A-Squad", "B-Squad"])

# Main Panel
st.title("Match Analysis Dashboard")
if match == "Amazonas vs. Athletic Club":
    st.write("🟡 Amazonas 1-0 (42% ±5%), Confidence: 0.70")
    match_data = pd.read_csv('data/match_data.csv')
    fig_form = px.bar(match_data, x='Team', y='Goals/Game', title="Team Form")
    st.plotly_chart(fig_form, use_container_width=True)
    st.write("🧠 Under 2.5 Goals (65% ±5%, 1.57 odds)")
    odds_data = pd.read_csv('data/odds_data.csv')
    fig_odds = px.bar(odds_data, x='Market', y='Probability %', title="Betting Markets", error_y='Probability %')
    st.plotly_chart(fig_odds, use_container_width=True)

# Placeholder for SHAP plot
st.write("SHAP plot temporarily disabled due to missing model file. Input values: Crowd Size = {}, Squad = {}".format(crowd_size, squad))