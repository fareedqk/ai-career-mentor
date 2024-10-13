from crewai import Crew
import logging

def execute_task(task):
    try:
        crew = Crew(
            agents=[task.agent],
            tasks=[task],
            verbose=True
        )
        return crew.kickoff()
    except Exception as e:
        logging.error(f"Error executing task: {str(e)}")
        raise