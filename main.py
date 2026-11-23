from agents.research_agent import ResearchAgent

research_agent = ResearchAgent()

print("Agent Name:", research_agent.name)
print("Agent Role:", research_agent.role)
print("Instructions:", research_agent.instructions)

result = research_agent.execute("Research the GenAI market")

print("Result:", result)