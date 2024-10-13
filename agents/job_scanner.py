from crewai import Agent, Task
from utils.custom_llm import CustomLLM

def create_job_scanner():
    return Agent(
        role='Job Scanner',
        goal='Scan job boards and provide detailed, relevant job recommendations based on the given profile',
        backstory='An AI agent specialized in analyzing job markets and identifying opportunities tailored to individual profiles. Known for providing comprehensive and structured job recommendations.',
        verbose=True,
        allow_delegation=False,
        llm=CustomLLM()
    )

def create_job_scan_task(agent, profile):
    return Task(
        description=f"""
        Analyze job boards and recommend the top 5 job postings for the following profile:
        Name: {profile.get('name', 'Not provided')}
        Years of experience: {profile.get('years_of_experience', 'Not provided')}
        Skills: {', '.join(profile.get('skills', ['Not provided']))}
        Desired role: {profile.get('desired_role', 'Not provided')}
        Preferred location: {profile.get('preferred_location', 'Not provided')}
        
        For each job posting, you MUST provide the following information in this exact format:

        [Job 1]
        Title: <job title>
        Company: <company name>
        Description: <brief job description in 1-2 sentences>
        Required Skills: <list of required skills>
        Salary Range: <salary range if available, otherwise "Not specified">
        Fit Reason: <why this job is a good fit for the profile>

        [Job 2]
        ...

        [Job 3]
        ...

        [Job 4]
        ...

        [Job 5]
        ...

        Ensure you provide exactly 5 job recommendations in this format. Do not include any additional text before or after the job listings.
        """,
        agent=agent,
        expected_output="""A list of 5 job recommendations, each containing:
        - Job title
        - Company name
        - Brief job description
        - Required skills
        - Salary range (if available)
        - Reason for fit with the given profile"""
    )