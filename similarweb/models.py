from datetime import datetime
from mongoengine import *


class PopularityHistory(EmbeddedDocument):
	world_rank = IntField()
	website_popularity = IntField()
	recorded_at = DateTimeField()
	created_at = DateTimeField(default=datetime.now)
	updated_at = DateTimeField(default=datetime.now)


class GeneralTraffic(EmbeddedDocument):
	direct = FloatField()
	referrals = FloatField()
	social = FloatField()
	search = FloatField()
	mail = FloatField()
	display = FloatField()
	created_at = DateTimeField(default=datetime.now)
	updated_at = DateTimeField(default=datetime.now)


class SocialTraffic(DynamicEmbeddedDocument):
	created_at = DateTimeField(default=datetime.now)
	updated_at = DateTimeField(default=datetime.now)


class Shop(Document):
	website = StringField(max_length=200, required=True)
	world_rank = IntField()
	website_popularity = IntField()
	recorded_at = DateTimeField()
	direct = FloatField()
	referrals = FloatField()
	social = FloatField()
	search = FloatField()
	mail = FloatField()
	display = FloatField()
	popularities = ListField(EmbeddedDocumentField(PopularityHistory))
	general_traffics = ListField(EmbeddedDocumentField(GeneralTraffic))
	social_traffics = ListField(EmbeddedDocumentField(SocialTraffic))
	created_at = DateTimeField(default=datetime.now)
	updated_at = DateTimeField(default=datetime.now)

	meta = { 'collection': 'shops' }


class DomainFeeder(Document):
	domain = StringField(max_length=200, required=True)
	created_at = DateTimeField(default=datetime.now)
	updated_at = DateTimeField(default=datetime.now)

	meta = { 'collection': 'domain_feeders' }
