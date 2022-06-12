from fastapi import FastAPI
from platform.events.router import events_router

app = FastAPI()
app.include_router(events_router)

@app.get("/")
def hello_bitcamp():
    return {"Hello": "Bitcamp 🔥"}
