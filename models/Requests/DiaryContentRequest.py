from pydantic import BaseModel

class DiaryContentRequest(BaseModel):
    content: str
    previous_topics: [str] | None