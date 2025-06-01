import requests
from bs4 import BeautifulSoup
import logging
import csv

class BookScraper: 
  base_URL = "http://books.toscrape.com/"
  
  def __init__(self):
      logging.basicConfig(level=logging.INFO) 
      self.logger = logging.getLogger("BookScaper")
          
  def fetch_page(self, url: str):
      try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
      except Exception as e:
        self.logger.error(f"Error web-source {url}: {str(e)}")
        raise
  
  def parse_books(self, soup: BeautifulSoup): #List[Dict]
     books = []
     for article in soup.select('article.product_pod'):
         title = article.h3.a['title']
         price = article.select('p.price_color')[0].text
         books.append({
             'title': title,
             'price': float(price)
         })
         self.logger.debug(f"Parsed book: {title}")
     return books

  def save_to_scv(self, books, filename: str = 'books.csv'):
      with open (filename, 'w', newline='') as f:
          writer = csv.DictWriter(f, fieldnames=['title', 'price'])
          writer.writehaeder()
          writer.writerows(books)
      self.logger.info(f'saved {len(books)} books to {filename}')
      
      
  def run(self):
      soup = self.fetch_page(self.base_URL)
      books = self.parse_books(soup)
      self.save_to_scv(books)     
      
if __name__ == "__main__":
    scraper = BookScraper()
    scraper.run()