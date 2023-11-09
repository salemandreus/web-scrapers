"""
A simple web scraper that parses html.
Input the site and css selector's full link.
"""

import bs4, requests

def getTextByCSSSelector(url, css_selector_path):
    """Takes a url and a css selector path from that page and returns the text from that selector path"""
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select(css_selector_path)
    return elems[0].text.strip() # remove any whitespace
