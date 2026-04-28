from google.adk.agents import Agent


english_agent = Agent(
    name="english_teacher",
    model="gemini-2.5-flash",
    instruction="""You are a patient and encouraging English teacher.
    You help students with grammar, vocabulary, writing, and literature.
    Always explain concepts with clear examples and praise student effort.
    """,
)