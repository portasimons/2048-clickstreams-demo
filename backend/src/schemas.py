from uuid import UUID
import enum
from datetime import datetime

from pydantic import BaseModel, NonNegativeInt


class EventType(enum.Enum):
    GameStart = "GameStart"
    GameRestart = "GameRestart"
    TilesMoveUp = "TilesMoveUp"
    TilesMoveDown = "TilesMoveDown"
    TilesMoveLeft = "TilesMoveLeft"
    TilesMoveRight = "TilesMoveRight"
    GameOver = "GameOver"
    Achieved2048 = "Achieved2048"


class UserEvent(BaseModel):
    """Класс для описания пользовательского события"""
    user_name: str
    timestamp: datetime
    event_type: EventType
    is_mobile_device: bool

class UserPersonalRecord(BaseModel):
    """Класс для описания персонального рекорда"""
    user_name: str
    timestamp: datetime
    score: NonNegativeInt
