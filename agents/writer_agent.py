
from agents.base_agent import BaseAgent


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Writer Agent",
            role="Report Writing Specialist",
            instructions="Create clear and structured reports using the information provided by other agents."
        )

    def execute(self, task: str) -> str:
        return f"{self.name} is preparing a report on: {task}"
