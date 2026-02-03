import math
import os

from .page import Page

PG_SIZE = 1024
PAGE_HEADER_SIZE = 8

class PageManager:
    last_page: Page

    def __init__(self, file_path: str):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, "wb"):
                pass

        file_size = os.path.getsize(self.file_path)
        if file_size == 0: 
            self.last_page = Page(0)
        else: 
            self.last_page = self.read_page(file_size // PG_SIZE - 1)
    
    def write_page(self, page: Page):
        with open(self.file_path, "rb+") as f:
            offset = page.page_id * PG_SIZE
            f.seek(offset)
            f.write(page.to_bytes())
            f.flush()

    def commit_changes_of_actual_page(self):
        with open(self.file_path, "rb+") as f:
            offset = self.last_page.page_id * PG_SIZE
            f.seek(offset)
            f.write(self.last_page.to_bytes())
            f.flush()

## Verificar Possivel loop
    def add_data(self, data):
        bytes_de_dados = bytes()

        if type(data) is int:
            bits = data.bit_length()
            bytes_necessarios = math.ceil(bits / 8) if bits > 0 else 1
            bytes_convertidos = data.to_bytes(bytes_necessarios, "little")
            bytes_de_dados = bytes_convertidos
        if type(data) is str: 
            bytes_convertidos = data.encode('utf-8')
            bytes_de_dados = bytes_convertidos
        
        try:
            self.last_page.insert_data(bytes_de_dados)
            self.commit_changes_of_actual_page()
        except: 
            self.last_page = Page(self.last_page.page_id + 1)
            self.add_data(data)

    def read_page(self, page_id: int) -> Page:
        with open(self.file_path, "rb+") as f:
            offset = page_id * PG_SIZE
            f.seek(offset)
            raw = f.read(PG_SIZE)

            if len(raw) != PG_SIZE:
                raise Exception("Page inexistente")

            return Page.from_bytes(raw)


