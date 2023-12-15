from read_data import games, games_links, programming, programming_links
from page_db import PageDataBase
from page_rank import page_rank
import pickle


page_db = PageDataBase()


for i in range(len(games)):
    page_db.generate_page(games[i]['url'], games[i]['words'], games_links[i]['link'])


for i in range(len(programming)):
    page_db.generate_page(programming[i]['url'], programming[i]['words'], programming_links[i]['link'])

h = page_db.pages[:4]

ranks = page_rank(page_db.pages)

def normalize_score(scores):
  max_value = max(scores)
  for i in range(len(scores)):
      scores[i] = float(scores[i]) / max(max_value, 0.00001)

normalize_score(ranks)

for j in range(len(page_db.pages)):
    page_db.pages[j].page_rank = ranks[j]

with open('page_db_instance.pkl', 'wb') as file:
    pickle.dump(page_db, file)
