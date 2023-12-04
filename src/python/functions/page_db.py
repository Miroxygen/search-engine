from page import Page


#Defines a simple structure for storing pages.
class PageDataBase:

    def __init__(self):
        self.pages = []
        self.word_dict = {}

    #Adds a page to the db.
    def add_page(self, page):
        self.pages.append(page)

    #Creates a page object from input data.
    def generate_page(self, url, words):
        page = Page(url)
        word_ids = []
        for word in words:
            word_id = self.get_word_id(word)
            word_ids.append(word_id)
        page.words = word_ids
        self.add_page(page)
    
    #If words exists in dictionary, return it's ID.
    #Else, add it to dictionary, create ID and return.
    def get_word_id(self, word):
        if word in self.word_dict:
            return self.word_dict[word]
        else:
            word_id = len(self.word_dict)
            self.word_dict[word] = word_id
            return word_id
