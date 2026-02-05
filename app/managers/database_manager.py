import os

from ..configuration import Const 
from .file_manager import FileManager
from .byte_manager import ByteManager

class DatabaseManager:
    def create_database(self):
        FileManager.create_file(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME)
        with FileManager.open_file(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME) as database_file: 
            database_header_data = bytearray(Const.DATABASE_HEADER_SIZE)
            database_header_data[0:4] = ByteManager.int_to_bytes(number=1, byte_quantity=4) # Espaco para versao
            database_header_data[4:10] = ByteManager.string_to_bytes("GUIZAO") # Espaco para o nome
            database_header_data[10:] = b'\x01' * 6
            database_file.write(bytes(database_header_data))
            database_file.flush()
            os.fsync(database_file.fileno())

    def start_database(self):
        if not os.path.exists(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME):
            self.create_database()
