from construct_db import page_db


def find_page_index(db, target_url):
        for index, page in enumerate(db.pages):
            if page.url == target_url:
                return index
        return -1

personal_computer_game = find_page_index(page_db, 'https://wikipedia.org/wiki/Adventure_game')

print(personal_computer_game)

print(len(page_db.pages[6].links))

def my_rank(this_page, page_db):
  url_prefix = "https://wikipedia.org"
  page_rank = 0.0
  array = []
  for page in page_db:
    if this_page.url.removeprefix(url_prefix) in page.links:
      page_rank += page.page_rank / len(page.links)
      array.append({'page rank':page_rank,'url' : page.url, 'pages rank' : page.page_rank,'num of links' : len(page.links)})
  page_rank = 0.15 + 0.85 * page_rank
  print(page_rank)
  return array

array = my_rank(page_db.pages[152], page_db.pages)

for i in array:
    print(i)