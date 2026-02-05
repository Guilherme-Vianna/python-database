from app.managers import DatabaseManager, DataManager

manager = DatabaseManager()
manager.start_database()
data_manager = DataManager()
