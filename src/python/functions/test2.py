from page_rank import page_rank

def my_rank(this_page, page_db):
  url_prefix = "https://wikipedia.org"
  page_rank = 0.0
  for page in page_db:
    if this_page.url.removeprefix(url_prefix) in page.links:
      page_rank += page.page_rank / len(page.links)
  page_rank = 0.15 + 0.85 * page_rank
  print(page_rank)

class TestPage:
    def __init__(self, url, links=None, page_rank=0.0):
        self.url = url
        self.links = links or []
        self.page_rank = page_rank

def test_page_rank():
    page_db = [
        TestPage("https://wikipedia.org/PageA", ["/PageA"]),
        TestPage("https://wikipedia.org/PageB", ["/PageA", 2, 3, 4], 0.5),
        TestPage("https://wikipedia.org/PageC", ["/PageA", 2, 3, 4, 5], 0.7),
        TestPage("https://wikipedia.org/PageD", ["/PageA"], 0.2),
    ]
    my_rank(page_db[0], page_db)

test_page_rank()
