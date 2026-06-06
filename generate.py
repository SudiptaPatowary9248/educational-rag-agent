from dotenv import load_dotenv
load_dotenv()

import os

from openai import OpenAI

from retrieve import retrieve_chunks
from strategy import detect_strategy
from prompts import build_prompt

from config import (
    LLM_MODEL,
    TEMPERATURE
)

# groq client
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

query = input("Enter query: ")

# retrieve
results = retrieve_chunks(query)

retrieved_chunks = results["documents"][0]

context = "\n\n".join(retrieved_chunks)

# strategy selection
strategy = detect_strategy(query)

# prompt building
prompt = build_prompt(
    strategy,
    context,
    query
)

# generation
response = groq_client.chat.completions.create(
    model=LLM_MODEL,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=TEMPERATURE
)

answer = response.choices[0].message.content

print("\nStrategy Used:", strategy)
print("\nGenerated Answer:\n")
print(answer)
