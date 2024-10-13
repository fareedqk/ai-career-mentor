import streamlit as st
from agents.job_scanner import create_job_scanner, create_job_scan_task
from utils.crew_manager import execute_task

def render_job_tab(user_data):
    st.subheader("Job Recommendations")
    
    if st.button("Get Job Recommendations"):
        with st.spinner("Scanning for jobs..."):
            job_scanner = create_job_scanner()
            job_scan_task = create_job_scan_task(job_scanner, user_data)
            result = execute_task(job_scan_task)
            
            # Post-process the result
            job_listings = parse_job_listings(result)
            
            # Display job listings
            for i, job in enumerate(job_listings, 1):
                with st.expander(f"Job {i}: {job['Title']} at {job['Company']}"):
                    st.write(f"**Description:** {job['Description']}")
                    st.write(f"**Required Skills:** {job['Required Skills']}")
                    st.write(f"**Salary Range:** {job['Salary Range']}")
                    st.write(f"**Why it's a good fit:** {job['Fit Reason']}")

def parse_job_listings(result):
    job_listings = []
    current_job = {}
    for line in result.split('\n'):
        line = line.strip()
        if line.startswith('[Job'):
            if current_job:
                job_listings.append(current_job)
            current_job = {}
        elif ':' in line:
            key, value = line.split(':', 1)
            current_job[key.strip()] = value.strip()
    if current_job:
        job_listings.append(current_job)
    return job_listings
