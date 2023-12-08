

#Defines a simple search engine.



class SearchEngine:

    def __init__(self, db):
        self.page_db = db

    #Searches the pages.
    def search(self, query):
        split_query = query.split()
        word_ids = []

        for query in split_query:
            id = self.page_db.get_word_id(query)
            word_ids.append(id)

        pages_matching_words = []
        word_frequency_per_page = []
        document_location_per_page = []
        page_rank_per_page = []

        for page in self.page_db.pages:
            if any(ids in page.words for ids in word_ids):
                pages_matching_words.append(page)
                word_frequency_per_page.append(self.word_frequency(word_ids, page.words))
                document_location_per_page.append(self.document_location(word_ids, page.words))
                page_rank_per_page.append(page.page_rank)
        if len(pages_matching_words) < 1 : #If no results, return.
            return 
        
        self.normalize_score(word_frequency_per_page, False)
        self.normalize_score(document_location_per_page)
        self.normalize_score(page_rank_per_page, False)
        result = []

        print(len(pages_matching_words))
        for i in range(len(pages_matching_words)):
            score = word_frequency_per_page[i] + 0.8 * document_location_per_page[i] + 0.5 * page_rank_per_page[i]
            result.append({"page" : pages_matching_words[i].url, "score" : round(score, 2) , "freq" : round(word_frequency_per_page[i], 2), "loc" : round((document_location_per_page[i] * 0.8), 2), "pr" : round((0.5 * page_rank_per_page[i]), 2)})
        sort = sorted(result, key=lambda x: x['score'], reverse=True)

        only_five = sort[:5]
        for s in only_five:
            print(s)
        return {"result" : sort[:5], "number" : len(pages_matching_words)}
        
    
    #Counts occurences of words in a page.
    def word_frequency(self, words, page):
        total_count = 0
        for word in words:
            total_count += (page.count(word))
        return total_count
    
    #Discovers how early words are in a page.
    def document_location(self, words, page):
        total_count = 0
        for query in words:
            found = False
            for i, word in enumerate(page):
                if query == word:
                    total_count += i + 1
                    found = True
                    break
            if not found:
                total_count += 100000
        return total_count
      
    #Normalizes scores.
    def normalize_score(self, scores, small=True):
        if(small) :
            min_value = min(scores)
            for i in range(len(scores)):
                scores[i] = float(min_value) / max(scores[i], 0.00001)
        else :
            max_value = max(scores)
            for i in range(len(scores)):
                scores[i] = float(scores[i]) / max(max_value, 0.00001)

