import streamlit as st

def render_sidebar():
    st.sidebar.header("User Profile")
    name = st.sidebar.text_input("Name")
    current_role = st.sidebar.text_input("Current Role")
    experience = st.sidebar.number_input("Years of Experience", min_value=0, max_value=50)
    skills = st.sidebar.text_area("Skills (comma-separated)")
    return {
        "name": name,
        "current_role": current_role,
        "experience": experience,
        "skills": skills
    }