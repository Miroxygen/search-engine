import pickle
from search_engine import SearchEngine
from construct_db import page_db

with open('page_db_instance.pkl', 'rb') as file:
    loaded_page_db = pickle.load(file)

search_engine = SearchEngine(page_db)

search_engine.search('java programming')