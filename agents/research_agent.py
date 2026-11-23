from agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Research Agent",
            role="Market Research Specialist",
            instructions="Research the given topic and provide relevant information."
        )

    def execute(self, task: str) -> str:
        return self.generate_response(task)