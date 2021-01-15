import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = 'https://www.livelib.ru/book/1003317448-garri-potter-i-uznik-azkabana-dzhoan-rouling'
"""data_content = {'title': [], 'authors': [], 'isbn': [], 'genre': [], 'characters': [],
                'setting': [], 'annotation': [], 'rating': [], 'reviews': []}"""
data_content = {'book_id': [], 'title': [], 'authors': [], 'rating': [], 'reviews': [], 'annotation': [],
                'publisher': [], 'isbn': [], 'genres': [], 'url': []}


def get_html_page(url):
    books_request = requests.get(url)
    books_request.encoding = 'utf8'
    books_content = books_request.text
    return books_content


'''def find_data(html_page, tag):
    parsed_page = BeautifulSoup(html_page, 'html.parser')
    data = parsed_page.find_all(tag)
    return data[0].text'''


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


if __name__ == '__main__':
    html_page = get_html_page(url)
    data_content['book_id'].append(url[28:38])
    add_data(find_data(html_page, 'h1', 'class', 'bc__book-title'), data_content['title'])
    add_data(find_data(html_page, 'a', 'class', 'bc-author__link'), data_content['authors'])
    add_data(float(str(find_data(html_page, 'span', 'itemprop', 'ratingValue')).replace(' ', '').replace(',', '.')),
             data_content['rating'])
    add_data(int(find_subdata(html_page, 'a', 'onclick', "return ll_tab(this, 'reviews', 'reviews');", 'b')[0]),
             data_content['reviews'])
    add_data(find_data(html_page, 'p', 'itemprop', 'description'), data_content['annotation'])
    add_data(find_subdata(html_page, 'td', 'itemprop', 'publisher', 'a'), data_content['publisher'])
    add_data(find_data(html_page, 'span', 'itemprop', 'isbn'), data_content['isbn'])
    add_data(find_subdata(html_page, 'ul', 'class', 'bc-genre__list', 'a'), data_content['genres'])
    data_content['url'].append(url)

