import os
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr



# ------------------------------
# Setup
# ------------------------------

load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPEN_AI_API_KEY is None:
    raise Exception("OPENAI_API_KEY is missing")
client = OpenAI(api_key=OPEN_AI_API_KEY)

# Retrieve key directly from environment variable
"""
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise Exception("OPENAI_API_KEY is missing")
client = OpenAI(api_key=api_key)
"""
# ------------------------------
# Document
# ------------------------------
document_overview = """
---
document_type: candidate_facts_overview
candidate_name: Hector Altamira
location: Murrieta, California
career_pivot: AI and Software Engineering
years_of_experience: 30+
education:
degree: Associate of Applied Science (AAS) in AI Software Engineering
institution: Maestro University
completion_year: 2026
primary_skills:
- Python Programming
- Software Engineering
- Frontend Development
- Technical Support
- Electronics
- AI Solution Development
---

# Hector Altamira - Career Overview & Core Facts

## Executive Summary & Core Strengths
- **Career Pivot:** Pivoting into AI and software engineering.
- **Experience:** Over 30 years of technical support and electronics experience.
- **Technical Focus:** Avid Python programmer specializing in AI, software projects, and frontend development for user-friendly web applications.
- **Location:** Based in Murrieta, California.
- **Passions:** Building innovative AI solutions, continuous learning, and mentoring/collaborating with developers and AI learners.

---

## Career History Highlights
- **Sr. Technical Support Engineer | Radisys (formerly Continuous Computing)** (2004–2013)
- Supported telecom OEMs with NSP and ATCA hardware/software.
- **Test Engineer | Lucent Technologies (formerly Ascend Communications)** (1997–2003)
- Supported telecom equipment manufacturers.
- **Sr. Electronics Technician | Amdahl Corporation** (1982–1997)
- Supported systems to component level, mainframe subsystems, and communications equipment.

---

## Writing & Publishing
- **Author Profile:** Published writer with 10 Kindle books focused on faith, hope, and knowing God.

---

## Additional Personal Context & Interests
- **Chess:** Actively played chess in 2001.
- **Culinary:** Enjoys cooking and trying new recipes; favorite dish to make is chili.
- **Travel & Cultural Exploration:** Has visited Japan, Germany, England, China, and North Korea.
- **Professional Interests:** Deeply interested in keeping up with new AI advancements and exploring new technologies and methods.
"""

# ------------------------------
# System Message
# ------------------------------
system_message = """
You are a digital twin of Hector Altamira, an AI and software engineering professional
with over 30 years of experience in technical support and electronics.
You have a strong background in Python programming, software engineering, frontend development,
and AI solution development. You are based in Murrieta, California, and are passionate
about building innovative AI solutions, continuous learning, and mentoring/collaborating
with developers and AI learners.

When people talk to you, you respond AS Hector - in the first person, using his voice, personality,
and knowledge. You are friendly, clear, and concise, making technical topics easy to understand.

Important: do not make things up. If you don't know the answer to a question, say "I don't know."
Do not invent or guess.

When the question asks for a list:
- Find every matching item in the context.
- Return every item; do not stop after the first few.
- Include items presented as bullets, headings, or sentences.
- Do not omit an item because it appears in a different chunk.
- Do not invent items that are not in the context.
- If the context is incomplete, say that the list may be incomplete.

Return one item per line.
"""


# ------------------------------
# Main Response Function
# ------------------------------
def respond_ai(user_message, history):
    system_message_enhanced = system_message + "\n\nContext:\n" + document_overview

    # Format full message list for OpenAI API
    messages = [{"role": "system", "content": system_message_enhanced}]

    # Format previous history
    for entry in history:
        if isinstance(entry, dict):
            messages.append(entry)
    messages.append({"role": "user", "content": user_message})

    # Call LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages
    )

    return response.choices[0].message.content


# ------------------------------
# Launch Gradio
# ------------------------------

gr.ChatInterface(fn=respond_ai).launch(inbrowser=True) #share=True to make it public
"""
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    gr.ChatInterface(
        fn=respond_ai,
        title="Hector Altamira Digital Twin",
        description="Ask questions to Hector Altamira's digital twin.",
    ).launch()

    #launch(server_name="0.0.0.0", server_port=port)
    """
