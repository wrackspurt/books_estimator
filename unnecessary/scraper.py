import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

data_content = {'book_id': [], 'title': [], 'authors': [], 'rating': [], 'reviews': [], 'annotation': [],
                'publisher': [], 'isbn': [], 'genres': [], 'url': []}


def get_html_page(url):
    books_request = requests.get(url)
    books_request.encoding = 'utf8'
    books_content = books_request.text
    return books_content


def find_data(html_page, tag, attr_type, attr_content):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    data = parsed_page.find(tag, attrs={attr_type: attr_content})
    return data.text


def find_subdata(html_page, tag, attr_type, attr_content, subattr):
    res = list()
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    data = parsed_page.find(tag, attrs={attr_type: attr_content})
    for d in data.find_all(subattr):
        res.append(d.text)
    return res


def add_data(data, lst):
    lst.append(data)
    return lst



