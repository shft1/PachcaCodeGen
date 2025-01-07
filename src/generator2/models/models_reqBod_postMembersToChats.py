from enum import Enum, IntEnum, StrEnum
from typing import Dict, Optional, List
from pydantic import Field, BaseModel


class Postmemberstochats(BaseModel):
    member_ids: List[int] = Field(..., description='Массив идентификаторов пользователей, которые станут участниками')
    silent: Optional[bool] = Field(None, description='Не создавать в чате системное сообщение о добавлении участника')


