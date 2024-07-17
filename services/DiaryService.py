import os
import json

import openai

from infrastructure.GeminiApi import GeminiApi
from infrastructure.OpenAIApi import OpenAiApi


class DiaryService:
    _gemini = GeminiApi()
    _openai = OpenAiApi()
    _system_instruction_file_path = os.environ["SYSTEM_INSTRUCTION_FILE_PATH"]
    _system_instruction = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DiaryService, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        with open(self._system_instruction_file_path) as json_file:
            self.system_instruction = json.load(json_file)

    ### Use Gemini API
    async def create_tags_from_diary_content(self, diary_content: str) -> str:
        """
        다이어리 내용으로 부터 태그들을 추출
        :param diary_content: 다이어리 내용
        :return: 다이어리 태그 목록(Emotion, People, Event, Place)
        """
        system_instruction = self.system_instruction["create_tags_system_instruction"]
        system_instruction = system_instruction.replace("{diary_content}", diary_content)
        return await self._gemini.generate_content_async(system_instruction, diary_content)

    async def create_suggested_topics_from_diary_content(self, diary_content: str) -> str:
        """
        다이어리 내용에서 장기 목표로 사용할 수 있는 내용들을 태깅
        :param diary_content: 다이어리 내용
        :return: 장기 목표가 태깅된 다이어리 내용
        """
        system_instruction = self.system_instruction["create_suggestions_system_instruction"]
        return await self._gemini.generate_content_async(system_instruction, diary_content)

    async def create_topics_from_diary_content(self, diary_content: str, previous_topics: [str]) -> [str]:
        """
        실시간 일기 내용의 모든 토픽을 생성
        :param diary_content: 다이어리 내용
        :param previous_topics: 기 추출 된 바 있는 토픽
        :return: 토픽 목록
        """
        system_instruction = self.system_instruction["create_diary_content_topics_system_instruction"]
        system_instruction = system_instruction.replace("{text}", diary_content)
        system_instruction = system_instruction.replace("{previous_topics}", str(previous_topics))
        return await self._gemini.generate_content_async(system_instruction, diary_content)

    async def create_embedding_from_diary_content(self, diary_content: str) -> str:
        """
        다이어리 내용으로 부터 임베딩 벡터 생성
        :param diary_content: 다이어리 내용
        :return: 임베딩 벡터 값
        """
        return await self._gemini.embed_content_async(diary_content)

    async def create_questions_from_user_information(self, user_information_list: [str]) -> [str]:
        """
        사용자 정보로 부터 질문을 생성
        :param user_information_list: 사용자 정보 목록
        :return: 질문 목록
        """
        system_instruction = self.system_instruction["create_question_system_instruction"]
        return await self._gemini.generate_content_async(system_instruction, user_information_list)

    ### Use ChatGPT API
    async def create_image_from_diary_content(self, diary_content: str) -> dict:
        """
        다이어리 내용으로 부터 이미지를 생성 (TODO: - Imagen으로 대체 가능 여부 확인)
        :param diary_content: 다이어리 내용
        :return: 이미지
        https://community.openai.com/t/dall-e-2-api-issue-billing-hard-limit-has-been-reached/22738/13
        """
        system_instruction = self.system_instruction["create_image_system_instruction"]
        system_instruction = system_instruction.replace('{text}', diary_content)
        supplement =  await self._gemini.generate_content_async(None, system_instruction)
        return await self._openai.generate_image_async(supplement)
