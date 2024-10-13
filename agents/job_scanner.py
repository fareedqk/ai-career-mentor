from crewai import Agent, Task
from utils.custom_llm import CustomLLM

def create_job_scanner():
    return Agent(
        role='Job Scanner',
        goal='Analyze real job listings and provide relevant recommendations based on the given profile',
        backstory='An AI agent specialized in analyzing job markets and identifying opportunities tailored to individual profiles.',
        verbose=True,
        allow_delegation=False,
        llm=CustomLLM()
    )

def create_job_scan_task(agent, profile, job_listings):
    job_listings_str = "\n\n".join([
        f"Job {i+1}:\nTitle: {job['title']}\nCompany: {job['company']['display_name']}\nDescription: {job['description']}\nLocation: {job['location']['display_name']}\nSalary: {job.get('salary_min', 'Not specified')} - {job.get('salary_max', 'Not specified')}"
        for i, job in enumerate(job_listings)
    ])

    return Task(
        description=f"""
        Analyze the following real job listings and recommend the top 5 that best match the given profile:

        Profile:
        Name: {profile.get('name', 'Not provided')}
        Years of experience: {profile.get('years_of_experience', 'Not provided')}
        Skills: {', '.join(profile.get('skills', ['Not provided']))}
        Desired role: {profile.get('desired_role', 'Not provided')}
        Preferred location: {profile.get('preferred_location', 'Not provided')}

        Job Listings:
        {job_listings_str}

        For each recommended job, provide the following information in this exact format:

        [Job 1]
        Title: <job title>
        Company: <company name>
        Description: <brief job description in 1-2 sentences>
        Location: <job location>
        Salary Range: <salary range if available, otherwise "Not specified">
        Fit Reason: <why this job is a good fit for the profile>

        [Job 2]
        ...

        Ensure you provide exactly 5 job recommendations in this format, choosing from the real job listings provided. Do not include any additional text before or after the job listings.
        """,
        agent=agent
    )