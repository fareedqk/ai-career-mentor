import streamlit as st
from agents.job_scanner import create_job_scanner, create_job_scan_task
from utils.crew_manager import execute_task

def render_job_tab(user_data):
    st.subheader("Job Recommendations")

    if st.button("Get Job Recommendations"):

        with st.spinner("Scanning for jobs..."):
            try:
                job_scanner = create_job_scanner()
                job_scan_task = create_job_scan_task(job_scanner, user_data)
                
                result = execute_task(job_scan_task)
                st.write(result)  # Debugging: See raw result

                job_listings = parse_job_listings(result)
                st.write(job_listings)  # Debugging: See parsed listings

                # Display job listings
                for i, job in enumerate(job_listings, 1):
                    with st.expander(f"Job {i}: {job.get('Title', 'N/A')} at {job.get('Company', 'N/A')}"):
                        st.write(f"**Description:** {job.get('Description', 'N/A')}")
                        st.write(f"**Required Skills:** {job.get('Required Skills', 'N/A')}")
                        st.write(f"**Salary Range:** {job.get('Salary Range', 'N/A')}")
                        st.write(f"**Why it's a good fit:** {job.get('Fit Reason', 'N/A')}")
            except Exception as e:
                st.error(f"An error occurred: {e}")


def parse_job_listings(result):
    job_listings = []
    current_job = {}
    for line in result.split('\n'):
        line = line.strip()
        if line.startswith('Job'):
            if current_job:
                job_listings.append(current_job)
            current_job = {}
        elif ':' in line:
            key, value = line.split(':', 1)
            current_job[key.strip()] = value.strip()
    if current_job:
        job_listings.append(current_job)
    return job_listings
