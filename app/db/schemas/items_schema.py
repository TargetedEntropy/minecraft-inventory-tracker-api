from datetime import date
from pydantic import BaseModel


class Items(BaseModel):
    uuid: str
    item_name: str

    class Conifg:
        orm_mode = True
