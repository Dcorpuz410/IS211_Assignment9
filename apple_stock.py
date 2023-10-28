if __name__ == "__main__":
    pass
mport requests
from bs4 import BeautifulSoup

# Set the URL you want to scrape
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

# Send an HTTP request to the URL and store the response
response = (url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Print the title of the page
print(soup.title.string)

# Print all the headings on the page
for heading in soup.find_all(['h1', 'h2', 'h3']):
  print(heading.string)