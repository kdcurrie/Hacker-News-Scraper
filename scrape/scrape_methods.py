'''
scrape.py
Python WebScraper designed to scrape hackernews website and sort through posts with over 100 upvotes
using Beautiful Soup web scraping library
'''

import requests
from bs4 import BeautifulSoup


def get_page_links(link, num_pages):
    '''
    generates a list of hackernews page links depending on a requested number of pages

    Parameters:
    link (list): a link for a specific hackernews page
    num_pages (int): the number of pages we want to scrape

    Returns:
    list: a list of the hackernews page links
    '''
    list_page_links = [link]

    for i in range(1, num_pages):
        list_page_links.append(f'{link}?p={i+1}')

    return list_page_links

def sort_stories_by_votes(hn_list):
    '''
    sorts a list of dictionary items by the number of votes in descending order

    Parameters:
    hn_list (list): an unsorted list of hackernews articles (in the form of dictionaries)

    Returns:
    list: A list of sorted article dictionary objects that contain the title,
    link, and number of votes

    '''
    return sorted(hn_list, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(list_links, list_subtext):
    '''
    generates a sorted list of hackernews links that have over 100 votes

    Parameters:
    links (list): list of .titlelink class which contains article titles and links
    subtext (list): list of .subtext class which contains the number of votes for the article

    Returns:
    list: A list of sorted article dictionary objects that contain the title,
    link, and number of votes

    '''
    hn_list = []
    for i, item in enumerate(list_links):
        title = item.getText()
        href = item.get('href', None)
        vote = list_subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn_list.append({'title': title, 'link' : href, 'votes': points})
    return sort_stories_by_votes(hn_list)


def create_mega_link_list(pages_links):
    '''
    generates a sorted list of hackernews articles that have over 100 votes

    Parameters:
    page_links (list): a list of hackernews page links

    Returns:
    list: a mega list of all of the articles from a given number of
    hackernews pages with over 100 votes
    '''
    links = []
    subtext = []
    mega_link_list = []

    for link in pages_links:
        res =  requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        links += soup.select('.titlelink') #. means that it's a class
        subtext += soup.select('.subtext')

    mega_link_list.append(create_custom_hn(links, subtext))

    return mega_link_list
