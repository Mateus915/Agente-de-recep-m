from crewai import Agent, Task
import yaml
from pathlib import Path
from src.hotel_ai.tools.custom_tool import registrar_baserow

# Define tools específicos por agente
AGENT_TOOLS = {
    "dispatcher": [registrar_baserow],
    "message_classifier": [],
    "response_agent": [],
}

def load_yaml(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

# Caminho dos arquivos YAML
CONFIG_DIR = Path(__file__).parent / "config"

agent_data = load_yaml(CONFIG_DIR / "agents.yaml")
task_data = load_yaml(CONFIG_DIR / "tasks.yaml")

# Criação dos agentes com ferramentas específicas
agents = {
    name: Agent(
        role=cfg["role"],
        goal=cfg["goal"],
        backstory=cfg["backstory"],
        verbose=True,
        tools=AGENT_TOOLS.get(name, [])  # Ferramentas específicas
    )
    for name, cfg in agent_data.items()
}

# Criação das tasks
tasks = {}
for name, cfg in task_data.items():
    agent_key = cfg["agent"]
    if agent_key not in agents:
        raise ValueError(f"Agente '{agent_key}' não encontrado para a tarefa '{name}'")
    tasks[name] = Task(
        description=cfg["description"],
        expected_output=cfg["expected_output"],
        agent=agents[agent_key],
    )
