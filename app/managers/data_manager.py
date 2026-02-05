from .page_manager import PageManager


class DataManager: 
    page_manager: PageManager
    
    def __init__(self):
        self.page_manager = PageManager()

    def add_data(self, data):
        self.page_manager.add_data(data)