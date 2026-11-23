from agents.base_agent import BaseAgent

class CompetitorAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Competitor Agent",
            role="Competitive Intelligence Specialist",
            instructions="Analyse competitor, their products, strengths, weaknesses, and market positioning."
        )

    def execute(self, task:str) -> str:
            return f"{self.name} is analyzing competitors: {task}"