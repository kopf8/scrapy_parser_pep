from pathlib import Path

PEP_URL = 'peps.python.org'
START_URL = 'https://peps.python.org/'
BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'
SUMMARY_FILENAME = 'status_summary'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_FORMAT = 'csv'
SUMMARY_TABLE_HEADERS = ('Статус', 'Количество')
SUMMARY_TABLE_LAST_ROW = 'Total'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
