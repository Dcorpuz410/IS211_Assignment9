import requests
from bs4 import BeautifulSoup

def get_football_stats():
    url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2023-season-regular-category-touchdowns"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='data')
        if table:
            rows = table.find_all('tr', class_=lambda x: x and 'row' in x.split())
            print(f"{'Rank':<5} {'Player':<25} {'Position':<10} {'Team':<20} {'Touchdowns':<10}")
            for row in rows[:20]:  # Limit to top 20 players
                rank = row.find('td', class_='cell-number').text.strip()
                player = row.find('td', class_='cell-player').text.strip()
                position = row.find('td', class_='cell-position').text.strip()
                team = row.find('td', class_='cell-team').text.strip()
                touchdowns = row.find('td', class_='cell-touchdowns').text.strip()
                print(f"{rank:<5} {player:<25} {position:<10} {team:<20} {touchdowns:<10}")
        else:
            print("Failed to find data table on the webpage.")
    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    get_football_stats()