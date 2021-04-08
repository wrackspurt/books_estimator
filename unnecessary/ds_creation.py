from unnecessary.scraper import get_html_page, find_data, find_subdata, add_data
from unnecessary.writer import get_links


def fill_in_dict(data_content, url):
    html_page = get_html_page(url)
    data_content['book_id'].append(url[28:38])
    add_data(find_data(html_page, 'h1', 'class', 'bc__book-title'), data_content['title'])
    add_data(find_data(html_page, 'a', 'class', 'bc-author__link'), data_content['authors'])
    add_data(str(find_data(html_page, 'span', 'itemprop', 'ratingValue')).replace(' ', '').replace(',', '.'),
             data_content['rating'])
    add_data(find_subdata(html_page, 'a', 'onclick', "return ll_tab(this, 'reviews', 'reviews');", 'b')[0],
             data_content['reviews'])
    add_data(find_data(html_page, 'p', 'itemprop', 'description'), data_content['annotation'])
    # add_data(find_subdata(html_page, 'td', 'itemprop', 'publisher', 'a'), data_content['publisher'])
    add_data(find_data(html_page, 'span', 'itemprop', 'isbn'), data_content['isbn'])
    add_data(find_subdata(html_page, 'ul', 'class', 'bc-genre__list', 'a'), data_content['genres'])
    data_content['url'].append(url)
    return data_content


links = get_links('links.txt')

data_content = {'book_id': [], 'title': [], 'authors': [], 'rating': [], 'reviews': [], 'annotation': [],
                'isbn': [], 'genres': [], 'url': []}


for l in links:
    fill_in_dict(data_content, l)


# write_data('books_data.csv', data_content)
