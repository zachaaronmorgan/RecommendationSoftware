from bs4 import BeautifulSoup
import requests


webpage_response = requests.get('https://www.metacritic.com/browse/game/?page=2',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
soup = BeautifulSoup(webpage_response.content, 'html.parser')

if webpage_response.status_code == 200:
    soup = BeautifulSoup(webpage_response.content, 'html.parser')
    print(soup.prettify())
    titles = soup.select(".c-finderProductCard_titleHeading")
    print(titles)
else:
    print(f"Failed to retrieve the webpage. Status code: {webpage_response.status_code}")