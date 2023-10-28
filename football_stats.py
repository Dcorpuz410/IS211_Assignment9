import urllib.request
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers/?sortcol=rutd&sortdir=descending"

def get_data(url):
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    return response

if __name__ == "__main__":
    page = get_data(url)
    soup = BeautifulSoup(page, 'html.parser')

    table = soup.find("table", class_="TableBase-table")
    # works table = soup.find("table", class_="TableBase-table")
    pretty_table = table.prettify()

    # print(pretty_table)
    # print(table)
    # print("======================================================================")
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if cells:
            player_name = cells[0].get_text()
            stats = [cell.get_text() for cell in cells[1:]]
            print(player_name, stats)
            # print(player_name)
    # print(soup)
    # print(soup.prettify())

    # table = soup.find('table', class_=)
    # print(table)

    # rows = table.prettify()

    # print("--------------------------------------------------")

    # print(rows)


    '''
    for row in rows:
        cells = row.find_all('td')
        for cell in cells:
            print(cell.get_text())
    '''