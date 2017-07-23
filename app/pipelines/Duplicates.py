# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class DuplicatesPipeline(object):
    def __init__(self):
        self.numbers = set()

    def process_item(self, item, spider):
        if item['number']:
            if item['number'] in self.numbers:
                raise DropItem('Duplicate pokeman found: %s' % item)
            else:
                self.numbers.add(item['number'])
                return item
        else:
            print('ERROR: item[\'number\'] is None')
