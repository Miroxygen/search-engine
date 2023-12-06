from read_data import games, games_links, programming, programming_links
from page_db import PageDataBase
from search_engine import SearchEngine


page_db = PageDataBase()

for i in range(len(games)):
    page_db.generate_page(games[i]['url'], games[i]['words'], games_links[i]['link'])


for i in range(len(programming)):
    page_db.generate_page(programming[i]['url'], programming[i]['words'], programming_links[i]['link'])

print(page_db.pages[1].url)
print(page_db.pages[1].links)

search_engine = SearchEngine(page_db)

#search_engine.search('java programming')
