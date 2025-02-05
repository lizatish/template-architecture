import uuid

from pydantic import BaseModel


class InputModel(BaseModel):
    id: uuid.UUID


class OutputModel(InputModel):
    name: str
    number: int
