from pathlib import Path
from app.configuration.header import Header
filename="data"
base_path=Path(filename)

class Engine:
    def create_db(self, page_size: int):
        header = Header().pack_header(total_pages=1)

        with open(filename, "wb") as f:
            f.write(header)
            f.write(b"\x00" * page_size)

        print("Banco criado com sucesso")


