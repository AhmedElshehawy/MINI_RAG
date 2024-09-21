import os
from .BaseController import BaseController


class ProjectController(BaseController):
    def __init__(self) -> None:
        super().__init__() 
        
    def get_project_path(self, project_id: str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )
        
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        
        return project_dir