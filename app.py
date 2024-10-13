import os
import streamlit as st
from ui.sidebar import render_sidebar
from ui.job_tab import render_job_tab
from ui.skill_tab import render_skill_tab
from litellm import set_verbose
from dotenv import load_dotenv
load_dotenv() 

def main():
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if groq_api_key is None:
        raise ValueError("GROQ_API_KEY environment variable is not set")
    # set_verbose(True)

    st.title("AI Career Mentor")

    user_data = render_sidebar()

    tab1, tab2, tab3 = st.tabs(["Job Recommendations", "Skill Analysis", "Interview Preparation"])

    with tab1:
        render_job_tab(user_data)

    with tab2:
        render_skill_tab(user_data)

    with tab3:
        st.markdown("# Interview Preparation Coming Soon!")

if __name__ == "__main__":
    main()