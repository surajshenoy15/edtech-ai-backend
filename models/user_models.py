from pydantic import BaseModel

class AdaptiveRequest(BaseModel):
    user_id: str
    topic: str
