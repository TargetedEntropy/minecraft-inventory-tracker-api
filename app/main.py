from fastapi import FastAPI
from fastapi_crudrouter import DatabasesCRUDRouter

from db.config import database
from db.schemas.items_schema import Items
from db.tables.items_table import items

description = """
Minecraft Inventory Tracker API
"""

app = FastAPI(root_path="", title="Minecraft Inventory Tracker API", description=description, version="0.1.0")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


router = DatabasesCRUDRouter(schema=Items, table=items, database=database)
app.include_router(router)
