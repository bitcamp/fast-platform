from platform.main import app
from tortoise.contrib.fastapi import register_tortoise
import os

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]

register_tortoise(
    app,
    db_url=f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
    modules={"models": ["__main__"]},
    generate_schemas=True,
    add_exception_handlers=True,
)