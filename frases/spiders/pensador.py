import scrapy
from frases.items import FrasesItem


class PensadorSpider(scrapy.Spider):
    name = 'pensador'
    allowed_domains = ['www.pensador.com']
    start_urls = ['https://www.pensador.com/autores/']
    url_base = 'https://www.pensador.com'
    locations = {'next_page': "//*[contains(text(), 'Próxima >')]/@href",
                 'phrases': '//*[@class="frase fr"]/text()',
                 'authors': '/html/body/div[1]/div[2]/div[1]/div[1]/div[3]/ul//a/@href'}


    def parse(self, response):
        authors = response.xpath(self.locations['authors']).extract()
        for author in authors:
            yield response.follow(f"{self.url_base}{author}", self.get_pages)

    def get_pages(self, response):
       
        next_page = response.xpath(self.locations['next_page']).extract()[0]
        author = response.url.split('/')[4]
        try:
            next_page = response.xpath(self.locations['next_page']).extract()[0]
            content = response.xpath(self.locations['phrases']).extract()
            yield FrasesItem(phrase=content,
                             author=author,
                             link=response.url)
            yield response.follow(f"{self.url_base}{next_page}", self.get_pages)
        except:
            author = response.url.split('/')[4]
            yield FrasesItem(phrase=content,
                             author=author,
                             link=response.url)
