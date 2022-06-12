from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.fastapi import pydantic_model_creator
from enum import Enum

class EventCategory(Enum):
    MAIN = 'main'
    MINI = 'mini'
    FOOD = 'food'
    WORKSHOP = 'workshop'
    SPONSORED = 'sponsored'
    

class Event(Model):
    '''An event that appears on the schedule'''

    # We chose 
    id = fields.UUIDField(pk=True)

    title = fields.CharField(max_length=256)
    description = fields.TextField()
    location = fields.CharField()
    tags = fields.JSONField() # JSON array of strings
    start_time = fields.DatetimeField()
    end_time = fields.DatetimeField()
    category = fields.CharEnumField(enum_type=EventCategory, max_length=32)
    favorites_count = fields.IntField()

    def __str__(self) -> str:
        return "<Event 'title'>"

EventPydantic = pydantic_model_creator(Event, name="Event")
EventPydanticIn = pydantic_model_creator(Event, name="EventIn", exclude_readonly=True)
