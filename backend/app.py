from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import src.db as db
from src.schemas import UserEvent, UserPersonalRecord

app = FastAPI()

origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post('/events')
async def save_user_event(event: UserEvent, request: Request):
    await db.save_event(event, request.client.host)
    return True


@app.post('/records')
async def save_user_record(record: UserPersonalRecord):
    await db.save_personal_record(record)
    return True
