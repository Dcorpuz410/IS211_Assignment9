import requests
from bs4 import BeautifulSoup

def get_nba_stats():
    url = "https://www.cbssports.com/nba/stats/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='data')
        if table:
            rows = table.find_all('tr', class_=lambda x: x and 'row' in x.split())
            print(f"{'Rank':<5} {'Player':<25} {'Team':<20} {'Points Per Game':<20}")
            for row in rows[:20]:  # Limit to top 20 players
                rank = row.find('td', class_='cell-number').text.strip()
                player = row.find('td', class_='cell-player').text.strip()
                team = row.find('td', class_='cell-team').text.strip()
                ppg = row.find('td', class_='cell-ppg').text.strip()  # Points per game column
                print(f"{rank:<5} {player:<25} {team:<20} {ppg:<20}")
        else:
            print("Failed to find data table on the webpage.")
    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    get_nba_stats()