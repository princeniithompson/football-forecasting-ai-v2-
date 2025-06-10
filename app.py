# Temporarily disable SHAP plot due to missing model file
# @st.cache_data
# def plot_shap(crowd_size, squad):
#     lightgbm_input = pd.DataFrame({
#         'crowd_size': [crowd_size], 'home_away': [1], 'form_streak': [1], 'relegation_context': [1]
#     })
#     if squad == "B-Squad":
#         lightgbm_input['form_streak'] = [0]
#     intensity_model = LGBMRegressor().load_model('models/lightgbm_intensity.pkl')
#     explainer = shap.TreeExplainer(intensity_model)
#     shap_values = explainer.shap_values(lightgbm_input)
#     shap_data = pd.DataFrame({
#         'Feature': ['Crowd Size', 'Home/Away', 'Form Streak', 'Relegation'],
#         'SHAP Value': shap_values[0]
#     })
#     fig_shap = px.bar(shap_data, x='Feature', y='SHAP Value', title="SHAP: Match Intensity")
#     return fig_shap
# st.plotly_chart(plot_shap(crowd_size, squad), use_container_width=True)
st.write("SHAP plot temporarily disabled due to missing model file.")