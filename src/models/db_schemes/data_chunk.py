from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class DataChunk(BaseModel):
    _id: Optional[ObjectId]
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    
    class Config:
        arbitrary_types_allowed = True