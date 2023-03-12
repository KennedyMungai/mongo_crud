"""The entrypoint to the project"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from database.connection import conn
from routes.events import event_router
from routes.users import user_router

app = FastAPI()

# Register routes
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

# Register origins
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def on_startup():
    """Connecting to the database on startup"""
    conn()


@app.get("/")
async def home():
    """The root endpoint

    Returns:
        RedirectResponse: Redirects response
    """
    return RedirectResponse(url="/event")


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
