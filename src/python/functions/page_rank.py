

def set_page_rank(this_page, page_db):
  url_prefix = "https://wikipedia.org"
  page_rank = 0.15
  for page in page_db:
    if this_page.url.removeprefix(url_prefix) in page.links:
      page_rank += 0.85 * (page.page_rank / (len(page.links)))
  #page_rank = 0.85 * page_rank
  return page_rank


def page_rank(page_db, iterations=20) :
  for _ in range(iterations):
    ranks = [(0.0)] * len(page_db) 
    for j in range(len(page_db)):
      ranks[j] = set_page_rank(page_db[j], page_db)
    for j in range(len(page_db)):
      page_db[j].page_rank = ranks[j]
