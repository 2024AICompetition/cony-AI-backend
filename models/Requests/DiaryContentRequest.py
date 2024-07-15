from typing import Optional
from pydantic import BaseModel

class DiaryContentRequest(BaseModel):
    content: str
    previous_topics: Optional[list[str]]