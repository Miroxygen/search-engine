import pickle
from search_engine import SearchEngine

with open('page_db_instance.pkl', 'rb') as file:
    loaded_page_db = pickle.load(file)

search_engine = SearchEngine(loaded_page_db)

search_engine.search('java programming')