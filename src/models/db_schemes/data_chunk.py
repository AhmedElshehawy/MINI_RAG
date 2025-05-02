from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field


class DataChunk(BaseModel):
    # fields that start with underscore can't be accessed, so we use them as an alias
    id: Optional[ObjectId] = Field(None, alias="_id")
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict
    chunk_order: int = Field(..., gt=0)
    chunk_project_id: ObjectId
    
    class Config:
        arbitrary_types_allowed = True