from pathlib import Path
import json
from datetime import datetime
import portalocker
filename="data.txt"
base_path=Path(filename)

class Engine:
    def database_exist(self) -> bool: 
        return base_path.exists()
    
    def put_object(self, object: dict):
        while True: 
            with open(filename, "a", encoding="utf-8") as file: 
                portalocker.lock(file=file, flags=portalocker.LOCK_NB | portalocker.LOCK_EX)
                file.write("\n" + str(object))
                break

    def start_database(self):
        creation_data = datetime.now().timestamp()
        database_data = { 
            "meta" :  {
                "creation_data": creation_data
            }
        }
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(database_data))
        
    def __init__(self):
        if not self.database_exist():
            self.start_database()

