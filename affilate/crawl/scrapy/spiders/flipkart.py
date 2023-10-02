import json

import django
import scrapy

django.setup()
from crawl.models import Item


class FlipKartSpider(scrapy.Spider):
    name = 'flipkart'
    start_urls = ['https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&q=best+offers&otracker=categorytree']

    def parse(self, response, **kwargs):
        json_data = json.loads(
            response.xpath(
                '//script[contains(text(),"window.__INITIAL_STATE__ = {")]//text()'
            ).get().replace(
                'window.__INITIAL_STATE__ = ',
                ''
            )[:-1])
        product_data = json_data.get(
            'pageDataV4'
        ).get('page').get('data')
        for product_key, item_list_dict in product_data.items():
            for item_dict in item_list_dict:
                if 'widget' in item_dict:
                    products_list = item_dict.get(
                        'widget', {}).get('data', {}).get(
                        'products') or []
                    for product in products_list:
                        mrp, price = '', ''
                        name = product.get('productInfo', {}).get('value', {}).get('titles', {}).get('title', '')
                        discount = product.get('productInfo', {}).get('value', {}).get('pricing', {}).get(
                            'totalDiscount') or ''
                        prices_data_list = product.get('productInfo', {}).get('value', {}).get('pricing', {}).get(
                            'prices') or []
                        for price_data in prices_data_list:
                            price_value = price_data.get('decimalValue')
                            if price_data.get('strikeOff'):
                                mrp = price_value
                            else:
                                price = price_value
                        product_url = product.get('productInfo', {}).get('value', {}).get('smartUrl') or ''
                        item = Item.objects.get_or_create(name=name, price=price)[0]
                        item.mrp = mrp
                        item.discount = discount
                        item.item_link = product_url
                        item.save()
