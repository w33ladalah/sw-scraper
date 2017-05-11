import scrapy

from similarweb.items import ShopItem
from similarweb.models import DomainFeeder


def read_feeder_data(criteria={}):
    try:
        domain_lists = []
        for domain_feeder in DomainFeeder.objects:
            domain_lists.append(domain_feeder['domain'])
        return domain_lists
    except Exception, e:
        print e


class SimilarWebSpider(scrapy.Spider):
    name = "similarweb"

    def start_requests(self):
        domains = read_feeder_data()
        for domain in domains:
            yield scrapy.Request(url="https://www.similarweb.com/website/" + domain, callback=self.parse)

    def parse(self, response):
        item = ShopItem()

        self._set_content_data(item, response)

        return item

    def _set_content_data(self, item, response):
        item['website'] = response.url
        item['direct'] = response.css("li.direct .trafficSourcesChart-value::text").extract_first()
        item['referrals'] = response.css("li.referrals .trafficSourcesChart-value::text").extract_first()
        item['search'] = response.css("li.search .trafficSourcesChart-value::text").extract_first()
        item['social'] = response.css("li.social .trafficSourcesChart-value::text").extract_first()
        item['mail'] = response.css("li.mail .trafficSourcesChart-value::text").extract_first()
        item['display'] = response.css("li.display .trafficSourcesChart-value::text").extract_first()

