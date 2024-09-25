import os

from aioch import Client

from src.schemas import UserEvent, UserPersonalRecord

CONN_URL: str = f"clickhouse://{os.environ['CH_USERNAME']}:{os.environ['CH_PASS']}@{os.environ['CH_HOST']}/{os.environ['CH_DBNAME']}"


async def save_event(user_event: UserEvent, net_address: str) -> None:
    client = Client.from_url(CONN_URL)

    inserted_row = (
        user_event.user_name, user_event.event_type.value, user_event.timestamp, net_address,
        user_event.is_mobile_device,
    )
    await client.execute("""
        INSERT INTO
            default.user_events (user_name, event_type, event_time, user_address, is_mobile)
        SETTINGS
            async_insert=1
        VALUES
        """,
        [inserted_row]
    )


async def save_personal_record(user_record: UserPersonalRecord) -> None:
    client = Client.from_url(CONN_URL)

    insert_row = (user_record.user_name, user_record.timestamp, user_record.score)
    await client.execute("""
        INSERT INTO
            default.personal_records (user_name, event_time, score)
        SETTINGS
            async_insert=1
        VALUES
        """,
        [insert_row]
     )
