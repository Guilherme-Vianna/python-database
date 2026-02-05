from ..configuration import Const
from ..managers.byte_manager import ByteManager
from .data_record import DataRecord

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
        self.used_bytes = 0
        self.data = bytearray(1016)
        self.records: list[DataRecord] = []
    
    def get_record_size(self, bytes) -> int: 
        size = ByteManager.int_from_bytes(bytes=bytes)
        return size

    def load_record(self, start_index = 0):
        record_size = self.get_record_size(self.data[start_index+1:start_index+7])
        if record_size == 0: 
            return
        record_bytes = bytes(self.data[start_index:start_index + record_size + Const.RECORD_HEADER_SIZE])
        record = DataRecord().from_bytes(bytes=record_bytes)
        self.records.append(record)
        self.load_record(start_index=start_index + record.get_bytes_size())

    def to_bytes(self) -> bytes: 
        page_byte_array = bytearray(1024)
        page_byte_array[0:4] = ByteManager.int_to_bytes(self.page_id, 4)
        page_byte_array[4:8] = ByteManager.int_to_bytes(self.used_bytes, 4)
        page_byte_array[8:1024] = self.data
        return bytes(page_byte_array)
    
    def from_bytes(self, page_bytes: bytes) -> 'Page':
        self.page_id = ByteManager.int_from_bytes(page_bytes[0:4])
        self.used_bytes = ByteManager.int_from_bytes(page_bytes[4:8])
        self.data = bytearray(page_bytes[8:1024]) 
        self.load_record()
        return self
    
    def add_record(self, record: DataRecord):
        if record.get_bytes_size() > 1016 - self.used_bytes: 
            raise Exception("pagina cheia")
        
        start_index = self.used_bytes
        end_index = start_index + record.get_bytes_size()
        self.data[start_index:end_index] = record.to_bytes()
        self.used_bytes += record.get_bytes_size()
