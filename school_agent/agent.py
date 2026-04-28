from google.adk.agents import Agent
from school_agent.agents.science_agent import science_agent
from school_agent.agents.maths_agent import maths_agent
from school_agent.agents.history_agent import history_agent
from school_agent.agents.english_agent import english_agent
from school_agent.agents.cs_agent import cs_agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Main router agent that sends tasks to sub-agents.",
    instruction= """
        You are the main assistant.

        Route user requests:
        - If user asks about physics, chemistry, biology, earth science, etc → use science_agent
        - If user asks about arithmetic, algebra, geometry, statistics, etc → use maths_agent
        - If user asks about ancient, medieval, modern history, etc → use history_agent
        - If user asks about grammar, vocabulary, writing, literature, etc → use english_agent
        - If user asks about computer science, programming, algorithms, etc → use cs_agent
        If unsure, respond directly.
    """,
    sub_agents=[science_agent, maths_agent, history_agent, english_agent, cs_agent]
)