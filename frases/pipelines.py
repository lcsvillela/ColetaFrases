# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class FrasesPipeline:
    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) 
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = open("arquivo.txt", 'w')

    def close_spider(self, spider):
        self.file.close()
