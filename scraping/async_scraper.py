import httpx
from parsel import Selector
import asyncio

class AsyncNewsScraper:
    Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',

}
    URL= 'https://www.scientificamerican.com/ecology/?page={page}&source='
    LINK_E = '//div[@class="grid__col large-up-8-12 section-latest"]/article/a/@href'
    PLUS_E = 'https://www.scientificamerican.com'


    async def async_genetator(self, limit):
        for page in range(1, limit):
            yield page



    async def parse_pages(self):
        async with httpx.AsyncClient(headers=self.Headers) as client:
            async for page in self.async_genetator(limit=4):
                await self.get_url(
                    client = client,
                    url = self.URL.format(
                        page=page
                    )
                )

    async def get_url(self, client, url):
        response = await client.get(url)
        print(response.url)
        await self.scrape_links(html=response.text, client=client)


    async def scrape_links(self, html, client):
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_E).extract()
        del links[-1]

        for link in links:
            print(link)

        return link[:5]


if __name__ == "__main__":
    scraper = AsyncNewsScraper()
    asyncio.run(scraper.parse_pages())
