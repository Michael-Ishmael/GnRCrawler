from django.test import TestCase

# Create your tests here.

from CrawlerManagement.business.data import CsvLoader


class TestCsvLoader(TestCase):
    def test_handle_uploaded_file(self):
        loader = CsvLoader()

        with open('/Users/funhead/Dev/Work/GNR/GnRCrawler/data/ShortComps.csv', 'rb') as f:
            companies = loader.handle_uploaded_file(f)
        self.assertTrue(len(companies) > 0)

