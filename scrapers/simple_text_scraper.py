"""
A simple web scraper that writes text to a file
Input the site url and a .txt file path to write to.
"""

import requests

def getScrapedText(url, output_file_path):
    res = requests.get(url)
    res.raise_for_status()

    outputFile = open(output_file_path, 'wb') #output to a file in write binary mode to maintain unicode encoding
    for chunk in res.iter_content(100000):
        outputFile.write(chunk)
