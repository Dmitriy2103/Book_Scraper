import unittest
from unittest.mock import patch
from scr.scraper import BookScraper
from bs4 import BeautifulSoup

class TestBookScrapper(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_page_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<html><body>Test</body></html>'
        
        scraper = BookScraper ()
        result = scraper.fetch_page("http://test.com")
        self.assertIsNotNone(result)
        
    def test_parse_books(self):
        test_html = """
        <article class="product_pod">
            <h3><a title="A Light in the Attic">Title</a></h3>
            <p class="price_color">£51.77</p>
        </article>
        """
        
        scraper = BookScraper()
        soup = BeautifulSoup(test_html, 'html.parser')
        books = scraper.parse_books(soup)
        self.assertEqual(books[0]['price'], 51.77)
        
