class Scraper:
    def __init__(self):
        self.__url = None
        self.__total_pages = 0
        self.__next_page_query_str = None

    @property
    def url(self) -> str:
        return self.__url

    # TODO add url validation w/ regex
    @url.setter
    def url(self, url: str) -> None:
        if not isinstance(url, str):
            print(f"Url must be of {str} not {type(url)}")
        else:
            self.__url = url

    @url.deleter
    def url(self) -> None:
        self.__url = None
        print("Url reset to None")


    @property
    def total_pages(self) -> str:
        return self.__total_pages

    @total_pages.setter
    def total_pages(self, num_of_pages: int) -> None:
        self.__total_pages = num_of_pages

    @total_pages.deleter
    def total_pages(self) -> None:
        self.__total_pages = 0
        print("Number of pages reset to 0")


hacker_news = Scraper()
hacker_news.url = "google.com"
print(hacker_news.url)
del hacker_news.url
print(hacker_news.url)