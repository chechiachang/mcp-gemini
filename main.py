import os

import chainlit as cl
from dotenv import find_dotenv
from dotenv import load_dotenv
from langfuse import get_client
from llama_index.core import Settings
from llama_index.llms.google_genai import GoogleGenAI
from loguru import logger
from openinference.instrumentation.llama_index import LlamaIndexInstrumentor

@cl.on_chat_start
async def start():
    load_dotenv(find_dotenv(), override=True)
    Settings.llm = GoogleGenAI(
        model=os.getenv("GOOGLE_GENAI_MODEL", "gemini-2.0-flash"),
        # api_key="some key",  # uses GOOGLE_API_KEY env var by default
        temperature=os.getenv("GOOGLE_GENAI_TEMPERATURE", 0.0),
    )

    langfuse = get_client()
    if langfuse.auth_check():
        logger.info("Langfuse client is authenticated and ready!")
    else:
        logger.warning("Langfuse client authentication failed. Please check your credentials and host.")
    LlamaIndexInstrumentor().instrument()

    await cl.Message(
       author="Assistant", content="Hello! Im an AI assistant. How may I help you?"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    logger.info(f"Received message: {message.content}")
    llm = Settings.llm
    response = llm.complete(message.content)
    await cl.Message(author="Assistant", content=response).send()
