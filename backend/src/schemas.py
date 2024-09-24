from uuid import UUID
import enum
from datetime import datetime

from pydantic import BaseModel


class EventType(enum.IntEnum):
    GameStart = 1


class UserEvent(BaseModel):
    """Класс для описания пользовательского события"""
    user_id: UUID
    timestamp: datetime
    event_type: EventType
    is_mobile_device: bool
