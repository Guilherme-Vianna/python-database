from io import BufferedRandom
import os

from ..configuration import Const

class FileManager: 
    @staticmethod
    def open_file(path: str): 
        if not os.path.exists(path):
            return open(path, "wb+")
        return open(path, "rb+")
    
    @staticmethod
    def create_file(path: str): 
        open(path, "x")

    @staticmethod
    def get_database_size(): 
        return os.path.getsize(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME)
    
    @staticmethod
    def get_database_file(): 
        return open(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME, "rb+")
    
    @staticmethod
    def save_file_to_disk(file: BufferedRandom): 
        file.flush()
        os.fsync(file.fileno())