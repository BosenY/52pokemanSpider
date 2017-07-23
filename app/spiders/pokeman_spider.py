#! /usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import re

from app.items import Pokeman


class pokemanSpider(scrapy.Spider):
    name = 'pokeman'

    # #001 妙蛙种子
    start_urls = ['https://wiki.52poke.com/wiki/%E5%A6%99%E8%9B%99%E7%A7%8D%E5%AD%90']

    def parse(self, response):
        def strip_text(text):
            if text is not None:
                return text.strip()

        for pokeman in response.css('#mw-content-text table.a-r.at-c'):
            pokeman_item = Pokeman()

            pokeman_item['name'] = pokeman.css(
                'tr:first-child td.roundy.bgwhite:first-child > span > b::text').extract_first()
            pokeman_item['jp_name'] = pokeman.css('tr:first-child span[lang=ja]::text').extract_first()
            pokeman_item['en_name'] = pokeman.css(
                'tr:first-child td.roundy.bgwhite:first-child > b:last-child::text').extract_first()
            pokeman_item['nature_img'] = pokeman.css(
                'tr:first-child td.roundy.bgwhite + td > a > img::attr(data-url)').extract_first()
            pokeman_item['number'] = pokeman.css('tr:first-child th.roundy.bgwhite > a::text').extract_first()
            pokeman_item['img'] = pokeman.css('tr:nth-child(2) img::attr(data-url)').extract_first()
            pokeman_item['attr'] = list(
                map(strip_text, pokeman.css('tr:nth-child(3) > td:first-child span > a::text').extract()))
            pokeman_item['category'] = strip_text(
                pokeman.css('tr:nth-child(3) > td:nth-child(2) td.roundy.bgwhite::text').extract_first())
            pokeman_item['features'] = pokeman.css(
                'tr:nth-child(4) > td:first-child td.roundy.bw-1 > a::text').extract()
            yield pokeman_item

        next_page_el = response.css('table.prenxt-nav > tr:nth-child(2) a:nth-child(1)')
        next_page_href = next_page_el.css('::attr(href)').extract()[4]
        next_page_text = next_page_el.css('::text').extract()[3]

        if re.search('No\.002', next_page_text) is None:
            next_page_href = response.urljoin(next_page_href)
            yield scrapy.Request(next_page_href, callback=self.parse)
