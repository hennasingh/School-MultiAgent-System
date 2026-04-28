from google.adk.agents import Agent

def calculate(expression: str) -> dict:
    """Evaluates a mathematical expression and returns the result."""
    try:
        result = eval(expression)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

maths_agent = Agent(
    name="maths_teacher",
    model="gemini-2.5-flash",
    instruction="""You are a patient and encouraging Maths teacher.
    You help students with arithmetic, algebra, geometry, and statistics.
    When solving problems, ALWAYS use your calculator tool for accuracy.
    Show step-by-step workings so students can follow along.""",
    tools=[calculate]
)