'''
scrape_example.py

Enter in a number of pages to scrape and this program will generate a list of hackernews articles
with over 100 votes
'''
import pprint
import scrape

NUM_PAGES = int(input("How many Hackernews pages would you like to scrape? "))
FIRST_PAGE_LINK = 'https://news.ycombinator.com/news'

print("Generating a list of Hackernews articles...")
page_links = scrape.scrape_methods.get_page_links(FIRST_PAGE_LINK, NUM_PAGES)
mega_links_list = scrape.scrape_methods.create_mega_link_list(page_links)
pprint.pprint(mega_links_list)
