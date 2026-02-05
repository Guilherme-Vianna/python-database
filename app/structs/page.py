from ..configuration import Const
from ..managers.byte_manager import ByteManager

"""
Estrutura de uma pagina

HEADER
page_id = 4 bytes
remaing_bytes = 4 bytes

DATA
data = 1016 Bytes

TOTAL = 1024 Bytes

"""

class Page:
    def __init__(self, page_id: int = 0):
        self.page_id = page_id
        self.remaing_bytes = 1016
        self.data = bytearray()
    
    def to_bytes(self) -> bytes: 
        page_byte_array = bytearray(1024)
        page_byte_array[0:4] = ByteManager.int_to_bytes(self.page_id, 4)
        page_byte_array[4:8] = ByteManager.int_to_bytes(1016, 4)
        return bytes(page_byte_array)
    
    def from_bytes(self, page_bytes: bytes) -> 'Page':
        page = Page()
        page.page_id = ByteManager.int_from_bytes(page_bytes[0:4])
        page.remaing_bytes = ByteManager.int_from_bytes(page_bytes[4:8])
        page.data = bytearray(page_bytes[8:1024]) 
        return page