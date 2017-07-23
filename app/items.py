# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Pokeman(Item):
    name = Field()
    jp_name = Field()
    en_name = Field()
    nature_img = Field()
    number = Field()
    img = Field()
    attr = Field()
    category = Field()
    features = Field()
