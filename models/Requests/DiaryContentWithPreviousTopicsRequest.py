from pydantic import BaseModel

class DiaryContentWithPreviousTopicsRequest(BaseModel):
    content: str
    previous_topics: list[str]