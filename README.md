# 🏫 School Multi-Agent System

An AI-powered school assistant built with **Google Agent Development Kit (ADK)** and **Gemini 2.5 Flash**. A root coordinator agent intelligently routes student questions to specialist subject agents — each with its own teaching personality and expertise.

---

## Architecture

```
Student Question
      │
      ▼
┌─────────────────┐
│   root_agent    │  ← coordinator / router
│ (Gemini 2.5     │
│  Flash)         │
└────────┬────────┘
         │  routes to
    ┌────┴─────────────────────────────────┐
    │                                      │
    ▼         ▼         ▼        ▼         ▼
english_   maths_   science_  history_   cs_
 agent     agent     agent     agent     agent
           │
        [calculate
           tool]
```

The **root agent** analyses each query and delegates to the appropriate subject specialist using ADK's native `sub_agents` + `transfer_to_agent` mechanism. The maths agent has access to a `calculate()` tool that evaluates mathematical expressions for accuracy.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent framework | [Google ADK](https://google.github.io/adk-docs/) |
| LLM | Gemini 2.5 Flash |
| Language | Python 3.12+ |
| Package manager | [uv](https://docs.astral.sh/uv/) |
| Local dev UI | ADK Web (`adk web`) |
| Deployment | Google Cloud Run |

---

## Project Structure

```
School-Multi-Agent-System/
├── .env                          ← GOOGLE_API_KEY (not to be committed)
├── .gitignore
├── .python-version
├── pyproject.toml
├── requirements.txt              ← for Cloud Run deployment
├── uv.lock
└── school_agent/
    ├── __init__.py               ← exports root_agent
    ├── agent.py                  ← root coordinator agent definition
    └── agents/
        ├── __init__.py
        ├── english_agent.py
        ├── maths_agent.py        ← includes calculate() tool
        ├── science_agent.py
        ├── history_agent.py
        └── cs_agent.py
```

---

## Agents

| Agent | Subjects | Tools |
|---|---|---|
| `english_teacher` | Grammar, vocabulary, writing, literature | — |
| `maths_teacher` | Arithmetic, algebra, geometry, statistics | `calculate()` |
| `science_teacher` | Physics, chemistry, biology, earth science | — |
| `history_teacher` | Ancient, medieval, modern history | — |
| `cs_teacher` | Programming, algorithms, computer systems | — |

---

## Running Locally

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) installed
- A Google API key from [Google AI Studio](https://aistudio.google.com/)

### Setup

```bash
# Clone the repo
git clone https://github.com/hennasingh/School-MultiAgent-System.git
cd School-Multi-Agent-System

# Create .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Install dependencies
uv sync

# Start the ADK web UI
uv run adk web .
```

Then open [http://localhost:8000](http://localhost:8000) in your browser, select `school_agent`, and start asking questions.

### Example prompts to try

- *"What is photosynthesis?"* → routes to science_agent
- *"Can you help me with long multiplication of 347 × 89?"* → routes to maths_agent (uses calculate tool)
- *"What caused World War 1?"* → routes to history_agent
- *"Explain what a for loop is"* → routes to cs_agent
- *"What's the difference between a metaphor and a simile?"* → routes to english_agent

---

## Key Concepts

**Multi-agent routing** — ADK's `sub_agents` parameter on the root agent allows it to delegate queries via `transfer_to_agent`. The transfer is visible in the ADK web UI's event log.

**Tool use** — The maths agent's `calculate()` function uses Python's `eval()` to evaluate expressions, returning a structured `{"status": "success", "result": ...}` dict. The agent always shows step-by-step workings alongside the computed result.

**Instruction design** — Each agent has a personality-led system prompt ("patient and encouraging") plus domain-specific guidance (e.g. "ALWAYS use your calculator tool for accuracy").

---

## Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Your Google AI Studio API key |

---