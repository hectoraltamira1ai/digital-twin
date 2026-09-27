import os
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import uuid
from pprint import pprint
import requests
import random
import chromadb
import json




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
document_overview ="""
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

document_education = """
---
document_type: education_and_certifications
candidate_name: Hector Altamira
degree_status: In Progress (AAS)
degrees:
- degree: Associate of Applied Science (AAS) in AI Software Engineering
institution: Maestro University
year: 2026
- degree: Electronic Engineering Technician
institution: DeVry Institute of Technology
certifications:
- AI Engineer Challenge Certificate (2026)
- Python Programming Certificate (2025)
- Frontend Developer Certificate (2024–2025)
- IT Computer Systems Training
- Online Coursework (Python 3, Linux)
---

# Hector Altamira - Education & Certifications

## Higher Education
- **Associate of Applied Science (AAS) in AI Software Engineering** (Enrolled / Completing) | Maestro University (2026)[cite: 4]
- **Electronic Engineering Technician Diploma/Degree** | DeVry Institute of Technology (Toronto, Canada)[cite: 4]

---

## Technical Certifications & Specialized Training
- **AI Engineer Challenge Certificate** | AI Engineer Challenge (2026)[cite: 4]
- **Python Programming Certificate** (2025)[cite: 4]
- **Frontend Developer Certificate** | Frontend Simplified (2024–2025)[cite: 4]
- **IT Computer Systems Training** | California Technical Academy (Temecula, CA)[cite: 4]
- **Online Coursework (Python 3, Linux)** | Coursera[cite: 4]
"""

document_professional_experience = """
---
document_type: resume
candidate_name: Hector Altamira
job_title: Technical Support / Test Engineer / Test Technician / Assembler
location: Murrieta, CA
address: 26181 Manzanita St., Murrieta, CA 92563
email: hector.altamira1@gmail.com
phone: 951-249-1371
primary_skills:
- Technical Support
- Test Engineering
- Component-Level Repair
- Failure Analysis
- Electro-Mechanical Assembly
- RMA Processing
- ISO 9000 Standards
- Linux
- Python
---

# Hector Altamira - Technical Support / Test Engineer / Test Technician / Assembler

## Contact Information
- **Full Name:** Hector Altamira
- **Address:** 26181 Manzanita St., Murrieta, CA 92563
- **Phone:** 951-249-1371
- **Email:** hector.altamira1@gmail.com
- **Target Roles:** Technical Support / Test Engineer / Test Technician / Assembler

---

## Professional Summary
Dynamic, self-motivated team player capable of multitasking, working effectively in an environment of changing priorities, and providing technical support to customers.

---

## Technical Skills & Certifications

### Certifications & Training
- Sun Certified Premier Systems Engineer
- A+ Certified
- Microsoft Windows 7 Certified
- IT Computer Systems Training (California Technical Academy)

### Operating Systems & Software
- **Operating Systems:** Microsoft Windows 7/8/10, Mac OS X, Linux Fedora 21, Microsoft Server 2012 R2
- **Tools & Platforms:** WebEx, VMware 7.1, Salesforce, ClearQuest, Microsoft Office Suite 2013, WordPress, Agile, AX

### Programming, Languages & Technologies
- Python 3, Linux, HTML5, CSS3, Ruby, Swift 2.0, Xcode 7.3, Sketch 3.7

---

## Professional Experience

### Operator III | Volt Staffing Agency (Assignment @ Abbott)
- **Location:** Temecula, CA
- **Duration:**  (2023 – 2025)

**Key Responsibilities:**
- Responsible for re-labeling medical devices using an industrial sealer.

---

### Owner & Certified Trauma Recovery Coach | HectorAltamiraCoaching, LLC
- **Website:** http://www.hectoraltamiracoaching.com
- **Duration:**  (2020 – 2025

**Key Responsibilities:**
- Operated an online business providing counseling services to clients in trauma recovery via Zoom.
- Managed all operational, administrative, and client-facing aspects of the business.

---

### Technical Support Engineer | Teledyne API
- **Location:** San Diego, CA
- **Duration:**  (2018 – 2020)

**Key Responsibilities:**
- Processed, repaired, tested, and calibrated Teledyne RMAs, focusing on Ozone air quality and process gas-monitoring instrumentation.
- Provided cost and material estimates to customers, managing workflow to ensure timely turnaround times.
- Performed PM and repaired RMAs to manufacturing specifications, providing certification of calibration.

---

### Electro-Mechanical Assembler III | Teledyne API
- **Location:** San Diego, CA
- **Duration:**  (2017 – 2018)

**Key Responsibilities:**
- Built and assembled complex units, including Teledyne T200, T201, T204, and T200M complete chassis builds.
- Built select sub-assemblies.

---

### Assembler | Staffmark (Assignment @ Denso)
- **Location:** Temecula, CA
- **Duration:** (2017 – 2017)

**Key Responsibilities:**
- Provided assembly support to the alternator teardown line, fully disassembling used alternators.
- Processed individual parts through cleaning, painting, and testing to remanufacture alternators.
- Utilized pneumatic power tools, presses, grinders, sandblasters, washers, Dremel tools, and custom equipment.

---

### Job Coach | Care-Rite Vocational Services
- **Location:** Temecula, CA
- **Duration:** (2017 – 2017)

**Key Responsibilities:**
- Provided one-on-one job and life skill coaching to consumers with Autism in the local community.
- Transported consumers to job and volunteering sites; taught goals and objectives set by social caseworkers.
- Wrote comprehensive weekly evaluations and progress reports; assisted consumers in accessing community resources.

---

### Program Manager, Technical Support | Redaptive LLC
- **Location:** San Diego, CA
- **Duration:** (2014 – 2017)

**Key Responsibilities:**
- Performed setup and execution of email marketing campaigns and acted as a liaison to third-party advertisers.
- Responsible for weekly metric reporting, improvement programs, account creation, and technical support.

---

### Sr. Technical Support Engineer | Radisys Corporation
- **Location:** San Diego, CA
- **Duration:** (2004 – 2013)

**Key Responsibilities:**
- Provided 24/7 on-call phone, email, and worldwide on-site technical troubleshooting during service maintenance windows on live systems.
- Processed, tested, and debugged RMAs; characterized and documented failures in internal repair databases (ClearQuest, Salesforce).
- Reconstructed customer failure modes in the lab for root cause analysis on DOAs; assisted engineering in design issue verification.
- Provided failure data to quality departments for continuous improvement and trained newly hired technical support personnel.

---

### Test Engineer | Lucent Technologies
- **Location:** Alameda, CA
- **Duration:** (1997 – 2003)

**Key Responsibilities:**
- Planned, developed, and conducted tests on remote access routers; developed Expect scripts for hardware test automation.
- Implemented functional test stations and provided 24/7 technical support to contract manufacturers (Solectron, Flextronics).
- Performed failure analysis on DOA/field returns and created Visio technical drawings and test procedures per ISO 9000 standards.

---

### Senior Electronic Technician | V-Tel
- **Location:** San Jose, CA
- **Duration:** (1996 – 1997)

**Key Responsibilities:**
- Performed functional and system tests on videoconference equipment and executed component-level repair of PCBs.
- Provided technical support to system technicians, trained new test personnel, and prepared quality control reports.

---

### Senior Electro-Mechanical Technician | Amdahl Corporation
- **Location:** Sunnyvale, CA
- **Duration:** (1991 – 1996)

**Key Responsibilities:**
- Conducted component-level repair of T1 Multiplexers, X.25 Concentrators, and Network Administrators.
- Served as Technical Expert for 4 product lines transferred from Toronto, Canada; established testing processes per ISO 9000 standards.

---

### Technical Support Technician D | Amdahl Communications Inc.
- **Location:** Toronto, Canada
- **Duration:** (1982 – 1991)

**Key Responsibilities:**
- Conducted component-level repair of T1 Multiplexers, X.25 Network Processors, concentrators, and administrators.
- Provided technical training and constructed prototype test fixtures for the Test Engineering Department.

---
"""

document_hobbies = """
---
document_type: profile_hobbies
candidate_name: Hector Altamira
location: Murrieta, CA
topics:
- Technical & Coding Interests
- Writing & Publishing
- Culinary Interests
- Outdoor Activities & Home Maintenance
primary_skills:
- Python
- Go
- Web Development
- OS Sandboxing
- Creative Writing & Self-Publishing
---

# Hector Altamira - Hobbies & Personal Interests

## Learning & Software Development
- **Advanced Programming:** Currently studying advanced Python and learning the Go programming language[cite: 3].
- **Projects:** Enjoys building websites and software applications designed to create isolated OS sandbox environments[cite: 3].

---

## Writing & Publishing
- **Author Profile:** Active, avid writer and published author with 10 books available on the Kindle Store[cite: 3].
- **Current Project:** In the final stages of publishing his latest book, *AI for Seniors*[cite: 3].

---

## Culinary Interests
- **Favorite Cuisines:** Avid foodie who enjoys exploring international cuisines, including Italian, Korean, Chinese, Mediterranean, and Indian[cite: 3].
- **Specialty:** Has created and perfected his own unique chili recipe[cite: 3].

---

## Outdoor Activities & Home
- **Outdoors:** Enjoys spending time outdoors and participating in off-road motorcycling whenever possible[cite: 3].
- **Home & Garden:** Active in home maintenance and gardening projects during leisure time[cite: 3].
"""

# ------------------------------
# Chunking Function
# ------------------------------
def split_text_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    # 1) Define preferred split points (from strongest to weakest boundary).
    boundaries = ["\n\n", "\n", ".", "?", "!", ",", " "]

    # 2) Helper: move chunk end to a natural boundary when possible.
    def find_boundary(start: int, end: int) -> int:
        midpoint = start + (chunk_size // 2)
        for boundary in boundaries:
            pos = text.rfind(boundary, midpoint, end)
            if pos != -1:
                return pos + len(boundary)
        return end

    # 3) Main loop: build chunks with overlap to preserve context.
    chunks: list[str] = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            end = find_boundary(start, end)
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = max(start + 1, end - overlap)
    return chunks


# ------------------------------
# RAG: Chunk, Embed, Store in ChromaDB
# ------------------------------
# 4) Run chunking and preview results.


documents = [
	{"text": document_overview, "source": "Overview Document"},
	{"text": document_education, "source": "Education & Certifications Document"},
	{"text": document_hobbies, "source": "Hobbies Document"},
	{"text": document_professional_experience, "source": "Professional Experience Document"}
]

chunks = []
ids = []
metadatas = []

for doc in documents:
    #Prepare the lists
    chunks_ = split_text_into_chunks(doc["text"], chunk_size=300, overlap =30)
    ids_ = [str(uuid.uuid4()) for _ in range(len(chunks_))]
    metadatas_ = [{"source": doc["source"], "chunk_index": i} for i in range(len(chunks_))]

    #Add to main lists
    chunks.extend(chunks_)
    ids.extend(ids_)
    metadatas.extend(metadatas_)
#Print for logging/debugging
print(f"Created {len(chunks)} chunks:\n")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} (ID: {ids[i]}, Source: {metadatas[i]['source']}, Index: {metadatas[i]['chunk_index']}, Length: {len(chunk)}):")
    print(chunk)
    print()

#Generate embeddings for all chunks
response = client.embeddings.create(
	model = "text-embedding-3-small",
	input = chunks
)

embeddings = [item.embedding for item in response.data]

#print(response)

#pprint(response.data)

#Verify embeddings for logging/debugging
print(f"Generated {len(embeddings)} embeddings")
print(f"Each embedding has {len(embeddings[0])} dimensions")

#Initialize ChromaDB and Store Vectors

# initialize ChromaDB client (persistent storage)
chroma_client = chromadb.PersistentClient(path ="./chroma_db_twin")

#Alternative initialize ChromaDB client (in-memory storage)
#chroma_client = chromadb.Client()

#Get or Create + Empty the collection before adding new data (for testing purposes)
collection = chroma_client.get_or_create_collection(name="digital_twin")
if collection.get()["ids"]:
    collection.delete(collection.get()["ids"])

#Adding data to ChromaDB collection
collection.add(
	ids=ids,
	embeddings=embeddings,
	documents=chunks,
	metadatas=metadatas
)

pprint(collection.get())

# ------------------------------
# Tools
# ------------------------------
tools = []

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

# Do not print secrets/tokens in notebook output
if not pushover_user or not pushover_token:
    raise Exception("PUSHOVER_USER or PUSHOVER_TOKEN missing. Ensure .env contains them, load_dotenv() ran in this kernel, and names match exactly.")

# Create send_notification function with basic error handling
def send_notification(message: str):
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    try:
        resp = requests.post(pushover_url, data=payload, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        # Raise a clearer error for callers to handle/log
        raise RuntimeError(f"Pushover request failed: {e}")
#Describe Pushover as an LLM tool
send_notification_function = {
    "name": "send_notification",
    "description": "Sends a push notification to the real-world version of you via Pushover on mobile. Use this to alert the real-world version of you about important events, completed tasks, or time-sensitive information.",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": "The notification message to send to the user's device"
            }
        },
        "required": ["message"]
    }
}

#Add Pushover to the list of tools for the LLM
tools.append({"type": "function", "function":send_notification_function})

#Simulates rolling a single six-sided dice
def dice_roll():
    result = random.randint(1,6)
    return result

#Describe function for the  LLM
roll_dice_function = {
    "name": "dice_roll",
    "description": "Simulates rolling a single six-sided dice and returns the result. Use this when the user wants to roll a dice for games, decisions, or random number generation",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": []
    }
}

#Add function to list of tools of LLM
tools.append({"type":"function", "function":roll_dice_function})





# ------------------------------
# Tool Handler
# ------------------------------


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

def respond_ai(message, history):
	#RAG Embed the query using the same model we used for the chunks to ensure compatibility
	response = client.embeddings.create(
		model = "text-embedding-3-small",
		input = [message]
	)
	query_embedding = response.data[0].embedding

	#RAG Search ChromaDB
	results = collection.query(
		query_embeddings=[query_embedding],
		n_results=15
	)


	retrieved_context = "\n\n".join(results["documents"][0])

	system_message = f"""
Answer using only the context below.

When the question asks for a list:
- Find every matching item in the context.
- Return every item; do not stop after the first few.
- Include items presented as bullets, headings, or sentences.
- Do not omit an item because it appears in a different chunk.
- Do not invent items that are not in the context.
- If the context is incomplete, say that the list may be incomplete.

Return one item per line.

Context:
{retrieved_context}
"""
	#RAG Stich retrieved chunks together to provide context for the response
	context = "\n---------\n".join(results["documents"][0])
	print("\n====================================")
	print(f"User message:\n{message}\n")
	print("***Retrieved Chunks:")
	for a, b in zip(results["documents"][0], results["metadatas"][0]):
		print("------------------------------------")
		print(f"<<Document {b['source']} --- Chunk {b['chunk_index']}>>\n{a}\n")
	#Update a system message with context (for this conversation turn)
	system_message_enhanced = system_message + "\n\nContext:\n" + context
	messages = [
    {"role": "system", "content": system_message},
    *history,
    {"role": "user", "content": message},
]
	response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages=messages
)
	reply = response.choices[0].message.content
	print("Reply:\n", reply) #Debugging line to see what the model is replying with.
	return reply

# ------------------------------
# Launch Gradio
# ------------------------------

gr.ChatInterface(fn=respond_ai).launch(inbrowser=True) #share=True to make it public

