class ByteManager(): 
    @staticmethod
    def int_to_bytes(number: int, byte_quantity: int | None = None) -> bytes: 
        if byte_quantity:
            return number.to_bytes(byte_quantity, "little")
        return number.to_bytes(number.bit_length(), "little")
    
    @staticmethod
    def int_from_bytes(bytes) -> int:
        return int.from_bytes(bytes, "little") 
    
    @staticmethod
    def string_to_bytes(text: str) -> bytes: 
        return text.encode('utf-8')