
#Defines a page for search engine.
class Page:

    def __init__(self, url):
        self.url = url
        self.words = []
        self.links = []
        self.page_rank = 1.0

