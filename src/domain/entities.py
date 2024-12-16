from uuid import UUID
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int

class User(BaseModel):

    id: UUID | str
    username: str
    phone_number: str

    token : Token
    