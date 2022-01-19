import urllib.request
from bs4 import BeautifulSoup as soup

def get_website(url):
    """
    scrapes html page for website
    """
    agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277"
    r = urllib.request.Request(url, headers= {'User-Agent' : agent})
    html = urllib.request.urlopen(r)
    page_soup_test = soup(html, "html.parser")

    return page_soup_test