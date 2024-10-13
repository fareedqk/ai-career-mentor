from crewai import Agent, Task
from utils.custom_llm import CustomLLM

def create_job_scanner():
    return Agent(
        role='Job Scanner',
        goal='Scan job boards and provide relevant job recommendations',
        backstory='An AI agent specialized in analyzing job markets and identifying opportunities',
        verbose=True,
        allow_delegation=False,
        llm=CustomLLM()
    )

def create_job_scan_task(agent, profile):
    return Task(
        description=f"""
        Analyze job boards and recommend the top 5 job postings for the following profile:
        {profile}
        
        For each job posting, provide:
        1. Job title
        2. Company name
        3. Brief job description (1-2 sentences)
        4. Required skills
        5. Salary range (if available)
        6. Why this job is a good fit for the profile

        Format the output as a numbered list.
        """,
        agent=agent
    )