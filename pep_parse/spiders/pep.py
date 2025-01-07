import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_URL, START_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_URL]
    start_urls = [START_URL]

    def parse(self, response):
        all_pep_links = response.css(
            'a.pep.reference.internal::attr(href)'
        ).getall()
        for pep_link in all_pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
