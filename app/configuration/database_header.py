VERSION = 1                  
MN = b"GUIZAO"
PG_SIZE = 1024
HEAD_SIZE = 10

class DatabaseHeader:
    def pack_header(self, total_pages: int) -> bytes:
        header = bytearray()

        header += MN                         
        header += VERSION.to_bytes(1, "little")           
        header += total_pages.to_bytes(3, "little")

        return bytes(header)
    
    def read_header(self, path):
        with open(path, 'rb') as f: 
            mn = f.read(6)
            version = int.from_bytes(f.read(1), "little")
            total_pages = int.from_bytes(f.read(3), "little")

        print(mn, version, total_pages)