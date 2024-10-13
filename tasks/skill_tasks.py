from crewai import Task

def analyze_skills(user_skills, agent):
    return Task(
        description=f"Analyze the following skills and suggest improvements: {user_skills}",
        agent=agent,
        expected_output="A detailed analysis of the user's skills, including strengths, areas for improvement, and 3-5 specific skill development recommendations."
    )