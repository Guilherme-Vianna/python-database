import math

PAGE_HEADER_SIZE = 8
PG_SIZE = 1024

class Page:
    def __init__(self, page_id: int):
        self.page_id = page_id
        self.used_bytes = 0
        self.data = bytearray()

    def insert_data(self, data: bytes):
        if self.used_bytes + len(data) > PG_SIZE - PAGE_HEADER_SIZE:
            raise Exception("Pagina não tem mais espaço")
        
        self.data[8+self.used_bytes:8+len(data)] = data
        self.used_bytes += len(data)

    @classmethod
    def from_bytes(cls, data_bytes: bytes) -> 'Page':
        if len(data_bytes) != PG_SIZE:
            raise ValueError(f"O buffer deve ter exatamente {PG_SIZE} bytes")

        page_id = int.from_bytes(data_bytes[0:4], "little")
        used_bytes = int.from_bytes(data_bytes[4:8], "little")
        
        page = cls(page_id)
        page.used_bytes = used_bytes
        page.data = bytearray(data_bytes[8:8 + used_bytes])
        
        return page

    def to_bytes(self) -> bytes:
        buffer = bytearray(PG_SIZE)

        buffer[0:4] = self.page_id.to_bytes(4, "little")
        buffer[4:8] = self.used_bytes.to_bytes(4, "little")

        buffer[8:8 + self.used_bytes] = self.data

        return bytes(buffer)