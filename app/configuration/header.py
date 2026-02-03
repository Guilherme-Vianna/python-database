VERSION = 1                  
MN = b"GUIZAO"
PG_SIZE = 1024
HEAD_SIZE = 10

class Header:
    def pack_header(self, total_pages: int) -> bytes:
        header = bytearray()

        header += MN                         
        header += VERSION.to_bytes(1, "little")           
        header += total_pages.to_bytes(3, "little")

        return bytes(header)