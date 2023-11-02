from parsel import Selector
import requests



class NewsScraper:
    URL = 'https://www.film.ru/compilation/luchshie-multfilmy-hayao-miyadzaki'
    LINK_A = '//div[@xmlns="http://www.w3.org/1999/html"]/div/a/@href'
    PLUS_A = 'https://www.film.ru'


    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_A).extract()

        for link in links:
            print(self.PLUS_U+link)

        return links[:5]





if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()
