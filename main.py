# from agents.research_agent import ResearchAgent

# research_agent = ResearchAgent()

# print("Agent Name:", research_agent.name)
# print("Agent Role:", research_agent.role)
# print("Instructions:", research_agent.instructions)

# result = research_agent.execute("Research the GenAI market")

# print("Result:", result)


# from agents.financial_agent import FinancialAgent

# financial_agent = FinancialAgent()

# print("\nAgent Name:", financial_agent.name)
# print("Agent Role:", financial_agent.role)

# result = financial_agent.execute("Analyze AI market revenue trends")

# print("Result:", result)

# from agents.competitor_agent import CompetitorAgent

# competitor_agent = CompetitorAgent()

# print("\nAgent Name:", competitor_agent.name)
# print("Agent Role:", competitor_agent.role)

# result = competitor_agent.execute(
#     "Analyze competitors in the AI chatbot market"
# )

# print("Result:", result)

from agents.writer_agent import WriterAgent

writer_agent = WriterAgent()

print("\nAgent Name:", writer_agent.name)
print("Agent Role:", writer_agent.role)

result = writer_agent.execute(
    "Prepare a report on the AI chatbot market"
)

print("Result:", result)