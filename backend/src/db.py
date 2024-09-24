import os

from aioch import Client

from src.schemas import UserEvent

CONN_URL: str = f"clickhouse://{os.environ['CH_USERNAME']}:{os.environ['CH_PASS']}@{os.environ['CH_HOST']}/{os.environ['CH_DBNAME']}"


async def insert_data(user_event: UserEvent, net_address: str) -> None:
    client = Client.from_url(CONN_URL)

    inserted_row = (
        str(user_event.user_id), str(user_event.event_type.name), user_event.timestamp, net_address,
        user_event.is_mobile_device,
    )
    await client.execute("""
        INSERT INTO
            default.user_events (user_id, event_type, event_time, user_address, is_mobile)
        SETTINGS
            async_insert=1
        VALUES
        """,
        [inserted_row]
    )
