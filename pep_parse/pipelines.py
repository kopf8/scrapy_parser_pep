import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import (DATETIME_FORMAT, FILE_FORMAT, RESULTS_DIR,
                                SUMMARY_FILENAME, SUMMARY_TABLE_HEADERS,
                                SUMMARY_TABLE_LAST_ROW)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counters = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counters[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'{SUMMARY_FILENAME}_{now_formatted}.{FILE_FORMAT}'
        file_path = self.results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as csv_file:
            csv.writer(
                csv_file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE,
            ).writerows([
                SUMMARY_TABLE_HEADERS,
                *self.status_counters.items(),
                (SUMMARY_TABLE_LAST_ROW, sum(self.status_counters.values())),
            ])
