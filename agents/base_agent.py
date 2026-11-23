from abc import ABC, abstractmethod
from google import genai

from config import GEMINI_API_KEY,GEMINI_MODEL

class BaseAgent(ABC):

    def __init__(self, name: str, role: str, instructions: str):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")
        self.name = name
        self.role = role
        self.instructions = instructions

        # Intialize Gemini client
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL

    def generate_response(self, task: str) -> str:
        prompt = f"""
        You are {self.name}.
        Your role: {self.role}.
        Instruction: {self.instructions}

        Task: {task}

        Provide a clear and useful response.
        """

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text or ""

    @abstractmethod
    def execute(self, task: str) -> str:
        pass