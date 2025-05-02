from typing import List
from bson import ObjectId
from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums import DataBaseEnum
from pymongo import InsertOne


class ChunkModel(BaseDataModel):
    def __init__(self, db_client) -> None:
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]
    
    async def create_chunk(self, chunk: DataChunk):
        try:
            result = await self.collection.insert_one(chunk.model_dump(by_alias=True, exclude_unset=True))
            chunk._id = result.inserted_id
            return chunk
        except Exception as e:
            # Log the error or handle it as appropriate for your application
            raise RuntimeError(f"Failed to create chunk: {e}")
        
    async def get_chunk(self, chunk_id: str):
        try:
            result = await self.collection.find_one({
                '_id': ObjectId(chunk_id)
            })
            
            if result is None:
                return None
            
            return DataChunk(**result)
        except Exception as e:
            # Log the error or handle it as appropriate for your application
            raise RuntimeError(f"Failed to get chunk with id {chunk_id}: {e}")
    
    async def insert_many_chunks(self, chunks: List[DataChunk], batch_size=100):
        try:
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i+batch_size]

                operations = [
                    InsertOne(chunk.model_dump(by_alias=True, exclude_unset=True))
                    for chunk in batch
                ]

                await self.collection.bulk_write(operations)
            
            return len(chunks)
        except Exception as e:
            # Log the error or handle it as appropriate for your application
            raise RuntimeError(f"Failed to insert many chunks: {e}")
    
    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        result = await self.collection.delete_many({'chunk_project_id': project_id})
        return result.deleted_count
