from app.engine import Engine
from app.services.page import Page
from app.services.page_manager import PageManager

engine = Engine()

page = Page(1)
page.insert_data(data="Guilherme")
page.insert_data(data="Mataveli")
page.insert_data(data="Goncalves")
page.insert_data(data="Vianna")
page.insert_data(data=100)
page.insert_data(data=256)
manager = PageManager(file_path="dados")
manager.write_page(page)
page = manager.read_page(1)
print(page)