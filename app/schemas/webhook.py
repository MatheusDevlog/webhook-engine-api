from pydantic import BaseModel, ConfigDict, Field


class WebhookPayload(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    message_id: str = Field(min_length=1, max_length=255)
    sender: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)


class WebhookResponse(BaseModel):
    status: str
    message_id: str
