from .data_type import DataType
from ..configuration.const import Const
from ..managers.byte_manager import ByteManager

'''
Estrutura 

HEADER
Type = 1 byte
Size = 7 byte

DATA
data = ??? Bytes

'''

class DataRecord: 
    type: DataType
    size: int
    data: bytes

    def get_bytes_size(self) -> int:
        return Const.RECORD_HEADER_SIZE + self.size

    def from_bytes(self, bytes: bytes) -> 'DataRecord':
        self.type = DataType(ByteManager.int_from_bytes(bytes[0:1])) 
        self.size = ByteManager.int_from_bytes(bytes[1:8])
        self.data = bytearray(bytes[8:8+self.size]) 
        return self
    
    def to_bytes(self) -> bytes:
        result = bytearray()
        result.extend(ByteManager.int_to_bytes(self.type.value, 1))
        result.extend(ByteManager.int_to_bytes(self.size, 7))
        result.extend(self.data)
        return bytes(result)