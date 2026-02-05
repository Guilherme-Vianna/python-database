class FileManager: 
    @staticmethod
    def open_file(path: str): 
        return open(path, "rb+")
    
    @staticmethod
    def create_file(path: str): 
        open(path, "x")