import os
from google import generativeai as genai


class GeminiApi:
    _gemini_api_key = os.environ["GEMINI_API_KEY"]
    _gemini_model = os.environ["GEMINI_MODEL"]

    def __new__(cls):
        if hasattr(cls, 'instance'):
            return cls.instance
        else:
            cls.instance = super(GeminiApi, cls).__new__(cls)

    def __init__(self):
        if self._gemini_api_key is None:
            raise Exception("환경변수(GEMINI_API_KEY)가 존재하지 않습니다.")
        if self._gemini_model is None:
            raise Exception("환경변수(GEMINI_MODEL)이 존재하지 않습니다.")
        genai.configure(api_key=self._gemini_api_key)

    async def generate_content_async(self, system_instruction: (str | None), text: str) -> str:
        if system_instruction is not None:
            model = genai.GenerativeModel(
                model_name=self._gemini_model,
                system_instruction=system_instruction
            )
        else:
            model = genai.GenerativeModel(
                model_name=self._gemini_model
            )
        response = await model.generate_content_async(text)
        response_text = response.text.strip()
        return response_text

    async def embed_content_async(self, text: str) -> [float]:
        response = await genai.embed_content_async(self._gemini_model, text)
        response_text = response.text.strip()
        return response_text
