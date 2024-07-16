from pydantic import BaseModel

class DiaryContentRequest(BaseModel):
    content: str
