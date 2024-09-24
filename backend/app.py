from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import src.db as db
from src.schemas import UserEvent

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
    await db.insert_data(event, request.client.host)
    return True
