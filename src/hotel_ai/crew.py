from crewai import Crew, Process
from .config_loader import agents, tasks

crew = Crew(
    agents=[agents["message_classifier"], agents["dispatcher"], agents["response_agent"]],
    tasks=[
        tasks["classify_message_task"],
        tasks["dispatch_task"],
        tasks["respond_client_task"]
    ],
    process=Process.sequential
)
