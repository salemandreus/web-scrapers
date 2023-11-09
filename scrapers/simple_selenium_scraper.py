from selenium import webdriver
from selenium.webdriver.common.by import By


def getElem(url, css_selector):
    """Takes strings 'url' and a unique css_selector path and returns the element matching"""
    browser = webdriver.Chrome()
    browser.get(url)
    elem = browser.find_element(By.CSS_SELECTOR, css_selector)
    return elem


def getElems(url, css_selector):
    """Takes strings 'url' and css_selector and returns all elements matching"""
    browser = webdriver.Chrome()
    browser.get(url)
    elems = browser.find_elements(By.CSS_SELECTOR, css_selector)
    return elems


def clickElement(url, css_selector):
    """Takes strings 'url' and a unique css_selector path and returns the element matching"""
    browser = webdriver.Chrome()
    browser.get(url)
    elem = browser.find_element(By.CSS_SELECTOR, css_selector)
    elem.click()
