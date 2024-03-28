import requests
import urllib.parse
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=1PHp1prsxIM&t=3395s"
encoded_url = urllib.parse.quote(url, safe=':/?=&')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
response = requests.get(encoded_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1", class_="title").text.strip()
view_count = soup.find("span", class_="view-count").text.strip()
published_date = soup.find("div", id="date").text.strip()

print("Title:", title)
print("View Count:", view_count)
print("Published Date:", published_date)