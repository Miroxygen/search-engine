from page_rank import page_rank

def my_rank(this_page, page_db):
  url_prefix = "https://wikipedia.org"
  page_rank = 0.15
  for page in page_db:
    if this_page.url.removeprefix(url_prefix) in page.links:
      page_rank += 0.85  * (page.page_rank / len(page.links))
  this_page.page_rank = page_rank

class TestPage:
    def __init__(self, url, links=None, page_rank=1.0):
        self.url = url
        self.links = links or []
        self.page_rank = page_rank

def test_page_rank():
    # Create a simple page database with three pages
    page_db = [
        TestPage("https://wikipedia.org/PageA", ["/PageA"]),
        TestPage("https://wikipedia.org/PageB", ["/PageA", 2, 3, 4]),
        TestPage("https://wikipedia.org/PageC", ["/PageA", 2, 3, 4, 5]),
        TestPage("https://wikipedia.org/PageD", ["/PageA"]),
    ]
    for _ in range(20):
      for i in range(len(page_db)):
        my_rank(page_db[i], page_db)
    
    for page in page_db:
        print(f"{page.url}: {page.page_rank}")

# Run the test
test_page_rank()
