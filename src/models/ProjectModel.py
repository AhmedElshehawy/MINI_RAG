from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from enums import DataBaseEnum
from math import ceil

class ProjectModel(BaseDataModel):
    def __init__(self, db_client) -> None:
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]
        
        
    async def create_project(self, project: Project):
        result = await self.collection.insert_one(project.model_dump())
        project._id = result.inserted_id
        return project
    
    
    async def get_project_or_create_one(self, project_id:str):
        record = await self.collection.find_one(
            {
                "project_id": project_id
            }
        )
        
        if record is None:
            # create new project
            project = Project(project_id=project_id)
            project = await self.create_project(project=project)
            return project    
        
        return Project(**record)
    
    async def get_all_projects(self, page: int=1, page_size: int=10):
        # count total number of douments
        # Cache total document count for optimization
        if 'total_documents_' not in self.__dict__:
            self.total_documents_ = await self.collection.count_documents({}) # empty dictionary to count all documents
        total_documents = self.total_documents_
        
        total_pages = ceil(total_documents / page_size) 
        
        # calculate number of total pages
        total_pages = ceil(total_documents / page_size)
        
        skip_count = (page-1) * page_size
        cursor = self.collection.find().skip(skip_count).limit(page_size)
        
        projects = []
        async for document in cursor:
            projects.append(Project(**document))
        
        return projects, total_pages
            
        
    
            