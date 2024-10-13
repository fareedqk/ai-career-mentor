from crewai import Task

def scan_jobs(user_profile, agent):
    return Task(
        description=f"Scan job boards and recommend jobs for a user with the following profile: {user_profile}",
        agent=agent,
        expected_output="A list of 3-5 job recommendations based on the user's profile, including job titles, companies, and brief descriptions."
    )