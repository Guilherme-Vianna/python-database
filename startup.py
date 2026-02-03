from app.engine import Engine
from app.services.page import Page
from app.services.page_manager import PageManager
import random

engine = Engine()
manager = PageManager(file_path="dados")

print(f"Data da pagina atual: {manager.get_page_data(manager.last_page.page_id)}")

# palavras = ['ABR1', 'ABC2', 'XVZ3', "CAS4"]

# for i in range(1000):
#     palavra = random.choice(palavras)
#     manager.add_data(palavra)

# manager.commit_changes_of_actual_page()
