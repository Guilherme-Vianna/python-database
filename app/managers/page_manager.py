import math
import os

from ..structs import Page, DataRecord, DataType
from ..configuration import Const
from .file_manager import FileManager
from .byte_manager import ByteManager

class PageManager:
    last_page: Page

    def __init__(self):
        if not self.database_have_pages():
            self.create_initial_page()
        self.load_last_page()

    def create_initial_page(self):
        page = Page(0) 
        with FileManager.get_database_file() as database_file: 
            database_file.seek(Const.DATABASE_HEADER_SIZE)
            database_file.write(page.to_bytes())
            FileManager.save_file_to_disk(database_file)

    def load_last_page(self):
        database_size = FileManager.get_database_size()
        page_count = math.ceil(( database_size - Const.DATABASE_HEADER_SIZE) / Const.PAGE_SIZE)  
        with FileManager.get_database_file() as database_file: 
            database_file.seek(int((page_count - 1) * Const.PAGE_SIZE + Const.DATABASE_HEADER_SIZE))
            page_bytes = database_file.read(Const.PAGE_SIZE)
            self.last_page = Page().from_bytes(page_bytes)

    def database_have_pages(self) -> bool: 
        return FileManager.get_database_size() != Const.DATABASE_HEADER_SIZE 
    
    def add_data(self, data):
        record = DataRecord()
        
        if type(data) is str:
            record.type = DataType.TEXT
            record.size = len(ByteManager.string_to_bytes(data))
            record.data = bytes(ByteManager.string_to_bytes(data)) 

        self.last_page.add_record(record=record)
        self.save_actual_page()
    
    def save_actual_page(self):
        with FileManager.get_database_file() as database_file:
            write_start_postion = Const.DATABASE_HEADER_SIZE + int(self.last_page.page_id * Const.PAGE_SIZE)
            database_file.seek(write_start_postion)
            database_file.write(self.last_page.to_bytes())
            FileManager.save_file_to_disk(database_file) 