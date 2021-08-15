from fastapi import FastAPI, Request

from .routers import api

app = FastAPI()
app.include_router(api.router)