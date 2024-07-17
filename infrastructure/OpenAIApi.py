import os
from openai import *

class OpenAiApi:
    _openai_api_key = os.environ["OPENAI_API_KEY"]
    openai = OpenAI()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OpenAiApi, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if self._openai_api_key is None:
            raise Exception("환경변수(OPENAI_API_KEY)가 존재하지 않습니다.")
        self.openai.api_key = self._openai_api_key

    async def generate_image_async(self, text: str) -> dict:
        try:
            response = self.openai.images.generate(
                model="dall-e-3",
                prompt=text,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response['data'][0]['url']
            return {"image_url": image_url}
        except OpenAIError as e:
            raise Exception(f"generate_image_async error: {e}")
