from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawl.scrapy.spiders.flipkart import FlipKartSpider


class Command:
    help = 'Run multiple Scrapy spiders concurrently'

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        spider_list = [FlipKartSpider]  # Replace with your actual spider names

        for spider_name in spider_list:
            process.crawl(spider_name)

        process.start()

    def process(self):
        self.handle()


if __name__ == '__main__':
    cls_obj = Command()
    cls_obj.process()
