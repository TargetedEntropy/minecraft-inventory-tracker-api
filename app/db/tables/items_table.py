import sqlalchemy

from db.config import metadata, engine

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("uuid", sqlalchemy.String),
    sqlalchemy.Column("item_name", sqlalchemy.String)
)

metadata.create_all(bind=engine)
