import os
import sys
import streamlit as st
import os, sys
sys.path.insert(0, './dashboard')

from multiapp import MultiApp
import model, user_engagement_analysis, user_experience_analytics, user_satisfaction_analysis,user_overview_analysis

st.set_page_config(page_title="Telecom User Data Visualization", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Telecom User Data Analysis
""")

# Add all your application here
app.add_app("user_overview",user_overview_analysis.app)
app.add_app("user_engagement", user_engagement_analysis.app)
app.add_app("experience_analytics", user_experience_analytics.app)
app.add_app("satisfaction_analysis", user_satisfaction_analysis.app)
app.add_app("Model", model.app)

# The main app
app.run()