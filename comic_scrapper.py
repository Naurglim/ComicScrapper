

class ComicScrapper:
    def __init__(self, search):
        self.search = search
        self.COMIC_SITE_BASE_URL = "https://comixextra.com/"
        self.COMIC_SITE_SEARCH = "search?keyword="
        self.COMIC_SITE_SEARCH_URL = COMIC_SITE_BASE_URL + COMIC_SITE_SEARCH
        self.COMIC_SITE_SEARCH_SEPARATOR = "+"
        self.FOLDER = "C:/Comics"

    
    def initial_url(self):
        keywords = self.search.split()
        search_string = self.COMIC_SITE_SEARCH_SEPARATOR.join(keywords)
        self.search_url = self.COMIC_SITE_SEARCH_URL + search_string


