from agents.base_agent import BaseAgent

class FinancialAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Financial Agent",
            role="Financial Analysis Specialist",
            instructions="Analyze financial data, identify trends, and provide financial insights."
        )

    def execute(self, task: str) -> str:
        return f"{self.name} is analyzing: {task}"