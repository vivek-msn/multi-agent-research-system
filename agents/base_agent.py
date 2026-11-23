
from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, name: str, role: str, instructions: str):
        self.name = name
        self.role = role
        self.instructions = instructions

    @abstractmethod
    def execute(self, task: str) -> str:
        pass