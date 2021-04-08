import csv


def get_links(path):
    links = list()

    with open(path) as file:
        for line in file.readlines():
            links.append(line.strip())
    return links


def write_data(path, data):
    with open(path, 'w', encoding='utf-8', errors='replace', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for d in range(len(data['book_id'])):
            writer.writerow((data['book_id'][d], data['title'][d], data['authors'][d],
                             data['rating'][d], data['reviews'][d], data['annotation'][d],
                             data['isbn'][d], data['genres'][d],
                             data['url'][d]))
