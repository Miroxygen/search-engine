from page_db import PageDataBase

#Defines a simple search engine.
class SearchEngine:

    def __init__(self):
        self.page_db = PageDataBase()

    def search(self, query):
        split_query = query.split()
        word_ids = []
        for query in split_query:
            id = self.page_db.get_word_id(query)
            word_ids.append(id)
        matching_pages = []
        for page in self.page_db.pages:
            if all(ids in page.words for ids in word_ids):
                matching_pages.append(page)
