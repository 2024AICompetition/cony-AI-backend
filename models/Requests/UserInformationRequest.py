from pydantic import BaseModel

class UserInformationRequest(BaseModel):
    user_information: list[str]