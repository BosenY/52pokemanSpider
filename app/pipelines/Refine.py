# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import re


class RefinePipeline(object):
    def process_item(self, item, spider):
        for (key, value) in item.items():
            if value is None:
                raise DropItem('None pokeman found: %s' % item)

        item['nature_img'] = 'https:' + item['nature_img']
        item['img'] = 'https:' + item['img']

        item['nature_img'] = item['nature_img'].replace('media.52poke.com', 's1.52poke.wiki')
        item['img'] = item['img'].replace('media.52poke.com', 's1.52poke.wiki')

        return item
