# adding debugs for prod issue
print("MAIN.PY IMPORTED")

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
templates = Jinja2Templates(directory="templates")

from retrieve import retrieve_chunks
from strategy import detect_strategy
from prompts import build_prompt

from openai import OpenAI
from dotenv import load_dotenv

from config import (
    LLM_MODEL,
    TEMPERATURE
)

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

print("CREATING FASTAPI APP")
app = FastAPI()
print("FASTAPI APP CREATED")

groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/ask")
def ask(query: str):

    try:
        results = retrieve_chunks(query)
        retrieved_chunks = results["documents"][0]

        logger.info(f"chunks_retrieved={len(retrieved_chunks)}")
        if retrieved_chunks:
            logger.info(f"top_chunk={retrieved_chunks[0][:100]}")

        context = "\n\n".join(retrieved_chunks)

        strategy = detect_strategy(query)

        logger.info(f"query={query}")
        logger.info(f"strategy={strategy}")

        prompt = build_prompt(
            strategy,
            context,
            query
        )

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

        return {
            "status": "success",
            "query": query,
            "strategy": strategy,
            "retrieved_chunks": retrieved_chunks,
            "answer": answer
        }

    except Exception as e:

        logger.error(f"error={str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }
