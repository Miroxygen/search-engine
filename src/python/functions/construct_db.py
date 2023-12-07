from read_data import games, games_links, programming, programming_links
from page_db import PageDataBase
from search_engine import SearchEngine
from page_rank import page_rank
import pickle


page_db = PageDataBase()

for i in range(len(games)):
    page_db.generate_page(games[i]['url'], games[i]['words'], games_links[i]['link'])


for i in range(len(programming)):
    page_db.generate_page(programming[i]['url'], programming[i]['words'], programming_links[i]['link'])

h = page_db.pages[:5]

page_rank(h)

with open('page_db_instance.pkl', 'wb') as file:
    pickle.dump(page_db, file)
