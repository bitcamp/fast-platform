from multiprocessing import Event
from platform.events.models import EventPydantic, EventPydanticIn
from typing import List
from fastapi import APIRouter

events_router = APIRouter(prefix="/events")

@events_router.post("/", response_class=EventPydantic)
async def add_event(event_in: EventPydanticIn):
    event = await Event.create(**event_in.dict())

@events_router.get("/", response_class=List[EventPydantic])
async def get_events():
    events = await EventPydantic.from_queryset(Event.all())
    print(f"{events=}")
    return events

