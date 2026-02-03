import os

from .page import Page

PG_SIZE = 1024

class PageManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, "wb"):
                pass
    
    def write_page(self, page: Page):
        with open(self.file_path, "rb+") as f:
            offset = page.page_id * PG_SIZE
            f.seek(offset)
            f.write(page.to_bytes())
            f.flush()

    def read_page(self, page_id: int) -> Page:
        with open(self.file_path, "rb+") as f:
            offset = page_id * PG_SIZE
            f.seek(offset)
            raw = f.read(PG_SIZE)

            if len(raw) != PG_SIZE:
                raise Exception("Page inexistente")

            return Page.from_bytes(raw)


