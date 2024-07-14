from fastapi import APIRouter, status
from models.Requests.DiaryContentRequest import  DiaryContentRequest

DiaryRouter = APIRouter(
    prefix="/v1/diaries", tags=["diary"]
)


@DiaryRouter.post("/images",
                  status_code=status.HTTP_201_CREATED)
async def create_image(diary_content: DiaryContentRequest):
    pass


@DiaryRouter.post("/tags",
                  status_code=status.HTTP_201_CREATED)
async def create_tags(diary_content: DiaryContentRequest):
    pass


@DiaryRouter.post("/embeddings",
                  status_code=status.HTTP_201_CREATED)
async def create_embedding(diary_content: DiaryContentRequest):
    # https://ai.google.dev/api/rest/v1/ContentEmbedding?hl=ko
    pass


@DiaryRouter.post("/suggested-topics",
                  status_code=status.HTTP_201_CREATED)
async def create_suggested_topics(diary_content: DiaryContentRequest):
    pass


@DiaryRouter.post("/diary-content-topics",
                  status_code=status.HTTP_201_CREATED)
async def create_diary_content_topics(diary_content: DiaryContentRequest):
    pass
