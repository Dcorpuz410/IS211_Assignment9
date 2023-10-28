import urllib.request
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_2023_box_office_number-one_films_in_the_United_States#In-Year_Release"

def get_data(url):
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response

if __name__ == "__main__":
    page = get_data(url)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', class_='wikitable')
    # print(table)

    # movies = soup.find_all('tr')
    rows = table.find_all('tr')
    # print(soup.prettify())

    # print("--------------------------------------------------")
    # print(soup.find(class_="wikitable sortable"))
    # print(rows)

    for row in rows:
        cells = row.find_all('td')
        for cell in cells:
            print(cell.get_text())