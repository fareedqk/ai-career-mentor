import streamlit as st
from agents.skill_analyzer import create_skill_analyzer, create_skill_analysis_task
from utils.crew_manager import execute_task

def render_skill_tab(user_data):
    st.subheader("Skill Analysis")
    
    if st.button("Analyze Skills"):
        with st.spinner("Analyzing skills..."):
            skill_analyzer = create_skill_analyzer()
            skill_analysis_task = create_skill_analysis_task(skill_analyzer, user_data)
            result = execute_task(skill_analysis_task)
            st.write(result)