import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from inngest.experimental import ai
from dotenv import load_dotenv
import uuid
import os
import datetime
load_dotenv()
inngest_client = inngest.Inngest(
     app_id = "rag_app",
    logging=logging.getLogger("uvicorn"),

)
print("hellow")
app = FastAPI()