

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
        matching_pages = []
        freq = []
        loc = []
        pr = []
        for page in self.page_db.pages:
            if any(ids in page.words for ids in word_ids):
                matching_pages.append(page)
                freq.append(self.word_frequency(word_ids, page.words))
                loc.append(self.document_location(word_ids, page.words))
                pr.append(page.page_rank)
           
        self.normalize_score(freq, False)
        self.normalize_score(loc)
        self.normalize_score(pr, False)
        result = []
        print(len(matching_pages))
        for i in range(len(matching_pages)):
            score = freq[i] + 0.8 * loc[i] + 0.5 * pr[i]
            result.append({"page" : matching_pages[i].url, "score" : round(score, 2) , "freq" : round(freq[i], 2), "loc" : round((loc[i] * 0.8), 2), "pr" : round((0.5 * pr[i]), 2)})
        sort = sorted(result, key=lambda x: x['score'], reverse=True)
        only_five = sort[:5]
        for s in only_five:
            print(s)
        
    
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

