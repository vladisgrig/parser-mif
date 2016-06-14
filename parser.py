from urllib.request import urlopen
from urllib.parse import urljoin

from lxml.html import fromstring


URL = 'http://www.mann-ivanov-ferber.ru/books/list/'
ITEM_PATH = '.books .books__item'

def parse_books():
	f = urlopen(URL)
	list_html = f.read().decode('utf-8')
	list_doc = fromstring(list_html)
	
	for elem in list_doc.cssselect(ITEM_PATH):
		book_name = elem.cssselect('.txt a')[0]
		book_name_txt = book_name.text
		book_href = book_name.get('href')	
		book_author = elem.cssselect('.book__author a')[0]
		book_author_txt = book_author.text
		print(book_name_txt,book_author_txt, book_href)

def main():
	parse_books()

if __name__ == '__main__':
	main()