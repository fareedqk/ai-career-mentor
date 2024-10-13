from crewai import Agent, Task
from utils.custom_llm import CustomLLM

def create_skill_analyzer():
    return Agent(
        role='Skill Analyzer',
        goal='Analyze the user\'s skills and provide recommendations for improvement',
        backstory='An AI agent specialized in assessing technical skills and suggesting learning paths',
        verbose=True,
        allow_delegation=False,
        llm=CustomLLM()
    )

def create_skill_analysis_task(agent, profile):
    return Task(
        description=f"""
        Analyze the following user profile and provide skill improvement recommendations:
        Name: {profile.get('name', 'Not provided')}
        Years of experience: {profile.get('years_of_experience', 'Not provided')}
        Skills: {', '.join(profile.get('skills', ['Not provided']))}
        Desired role: {profile.get('desired_role', 'Not provided')}
        Preferred location: {profile.get('preferred_location', 'Not provided')}
        
        1. List the user's current skills
        2. Identify any skill gaps based on their desired role
        3. Suggest 3-5 skills to learn or improve
        4. Provide resources (online courses, books, etc.) for each suggested skill
        5. Estimate the time required to acquire or improve each skill

        Format the output in a clear, easy-to-read structure.
        """,
        agent=agent
    )