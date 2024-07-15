from fastapi import APIRouter, status
from models.Requests.DiaryContentRequest import DiaryContentRequest
from models.Requests.UserInformationRequest import UserInformationRequest
from services.DiaryService import DiaryService

DiaryRouter = APIRouter(
    prefix="/v1/diaries", tags=["diary"]
)

diary_service = DiaryService()


@DiaryRouter.post("/tags",
                  status_code=status.HTTP_201_CREATED)
async def create_tags(diary_content_reqeust: DiaryContentRequest):
    """
     다이어리 내용으로 부터 태그들을 추출
    :request diary_content_reqeust:
        {
            "content": string
        }
    :response:
    """
    return await diary_service.create_tags_from_diary_content(diary_content_reqeust.content)


@DiaryRouter.post("/suggested-topics",
                  status_code=status.HTTP_201_CREATED)
async def create_suggested_topics(diary_content_reqeust: DiaryContentRequest):
    """
     다이어리 내용에서 장기 목표로 사용할 수 있는 내용들을 태깅
    :request diary_content_reqeust:
        {
            "content": string
        }
    :response:
    """
    return await diary_service.create_suggested_topics_from_diary_content(diary_content_reqeust.content)


@DiaryRouter.post("/diary-content-topics",
                  status_code=status.HTTP_201_CREATED)
async def create_diary_content_topics(diary_content_reqeust: DiaryContentRequest):
    """
     실시간 일기 내용의 모든 토픽을 생성
    :request diary_content_reqeust:
        {
            "content": string,
            "previous_topics": [string]
        }
    :response:
    """
    return await diary_service.create_topics_from_diary_content(diary_content_reqeust.content,
                                                                diary_content_reqeust.previous_topics)


@DiaryRouter.post("/embeddings",
                  status_code=status.HTTP_201_CREATED)
async def create_embedding(diary_content_reqeust: DiaryContentRequest):
    """
     다이어리 내용으로 부터 임베딩 벡터 생성
    :request diary_content_reqeust:
        {
            "content": string
        }
    :response:
    """
    # https://ai.google.dev/api/rest/v1/ContentEmbedding?hl=ko
    return await diary_service.create_embedding_from_diary_content(diary_content_reqeust.content)


@DiaryRouter.post("/diary-content-topics",
                  status_code=status.HTTP_201_CREATED)
async def create_question(user_information_request: UserInformationRequest):
    """
     사용자 정보로 부터 질문을 생성
    :request user_information_request:
        {
            "user_information": [string]
        }
    :response:
    """
    return await diary_service.create_questions_from_user_information(user_information_request.user_information)

@DiaryRouter.post("/images",
                  status_code=status.HTTP_201_CREATED)
async def create_image(diary_content_reqeust: DiaryContentRequest):
    """
    다이어리 내용으로 부터 이미지를 생성
    :request diary_content_reqeust:
        {
            "content": string
        }
    :response:
    """
    return await diary_service.create_image_from_diary_content(diary_content_reqeust.content)
