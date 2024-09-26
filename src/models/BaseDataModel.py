from helpers.config import get_settings, Settings


class BaseDataModel:
    def __init__(self, db_client) -> None:
        self.db_client = db_client
        self.app_settings = get_settings()
    
    