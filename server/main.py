from fastapi import FastAPI
import logging
from .routers import apiRouter
from .database.database import create_db, dispose_db
from .migration.migration import migrate_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

app = FastAPI()
app.include_router(apiRouter)


@app.on_event("startup")
async def startup():
    await create_db()
    await migrate_db()


@app.on_event("shutdown")
async def shutdown():
    await dispose_db()
