import os

from ..configuration import Const 
from .file_manager import FileManager
from .byte_manager import ByteManager

"""
Estrutura do Header do banco de dados

HEADER
versao = 4 bytes
nome = 6 bytes
livres = 6 bytes

TOTAL = 16 Bytes

"""

class DatabaseManager:
    def create_database(self):
        with FileManager.open_file(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME) as database_file: 
            database_header_data = bytearray(Const.DATABASE_HEADER_SIZE)
            database_header_data[0:4] = ByteManager.int_to_bytes(number=1, byte_quantity=4) # Espaco para versao
            database_header_data[4:10] = ByteManager.string_to_bytes("GUIZAO") # Espaco para o nome
            database_file.write(bytes(database_header_data))
            FileManager.save_file_to_disk(database_file)

    def start_database(self):
        if not os.path.exists(Const.DEFAULT_PATH + Const.DATABASE_DEFAULT_NAME):
            self.create_database()
