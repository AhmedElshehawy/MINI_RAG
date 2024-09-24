import os
from .BaseController import BaseController
from .ProjectController import ProjectController
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from models import ProcessingEnum
from langchain_text_splitters import RecursiveCharacterTextSplitter


class ProcessController(BaseController):
    def __init__(self, project_id: str) -> None:
        super().__init__()
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)
    
    def get_file_extension(self, file_id: str):
        extension = os.path.splitext(file_id)[-1]
        return extension
    
    def get_file_loader(self, file_id: str):
        file_extension = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )
        if file_extension==ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding='utf-8')
        if file_extension==ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        return None
    
    def get_file_content(self,  file_id:str):
        loader = self.get_file_loader(file_id=file_id)
        return loader.load()
    
    def process_file_conent(self, file_content: list, chunk_size: int = 100, overlap_size = 20):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
        )
        file_contnet_texts = [
            record.page_content
            for record in  file_content
        ]

        file_metadata = [
            record.metadata
            for record in file_content
        ]
        
        chunks = text_splitter.create_documents(
            file_contnet_texts,
            metadatas=file_metadata
        )
        
        return chunks