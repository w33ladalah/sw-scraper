# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urlparse import urlparse
from similarweb.models import GeneralTraffic, Shop


def _clean_percent_character(data):
	return data.replace("%", "")

def _convert_to_number(data):
	return float(data)


class ExtractDomainNamePipeline(object):
	def process_item(self, item, spider):
		item['website'] = item['website'].replace("https://www.similarweb.com/website/", "")

		return item


class ConvertToIntGeneralTrafficPipeline(object):
    def process_item(self, item, spider):
    	item['direct'] = _convert_to_number(_clean_percent_character(item['direct']))
    	item['referrals'] = _convert_to_number(_clean_percent_character(item['referrals']))
    	item['search'] = _convert_to_number(_clean_percent_character(item['search']))
    	item['social'] = _convert_to_number(_clean_percent_character(item['social']))
    	item['mail'] = _convert_to_number(_clean_percent_character(item['mail']))
    	item['display'] = _convert_to_number(_clean_percent_character(item['display']))

        return item


class SaveGeneralTrafficPipeline(object):
	def process_item(self, item, spider):
		try:
			last_traffic = Shop.objects(website=item['website']).first()

			if last_traffic.direct != item['direct']:
				self._save_parent_traffic(item)
				self._save_embedded_traffic(item, 'update')
		except Exception as e:
			self._save_parent_traffic(item)
			self._save_embedded_traffic(item)

		return item

	def _save_parent_traffic(self, item):
		shop = Shop.objects(website=item['website']).update_one(direct=item['direct'],
	        referrals=item['referrals'],
	        search=item['search'],
	        social=item['social'],
	        mail=item['mail'],
	        display=item['display'])

	def _save_embedded_traffic(self, item, mode='new'):
		general_traffic = GeneralTraffic(direct=item['direct'])
		general_traffic.referrals = item['referrals']
		general_traffic.search = item['search']
		general_traffic.social = item['social']
		general_traffic.mail = item['mail']
		general_traffic.display = item['display']

		if mode == 'new':
			shop = Shop.objects(website=item['website']).update_one(general_traffics=[general_traffic])
		else:
			shop = Shop.objects(website=item['website']).update_one(push_general_traffics=general_traffic)
