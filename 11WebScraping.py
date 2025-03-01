import requests
from bs4 import BeautifulSoup

url = 'https://google.com'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')

    text_content = soup.get_text()
    print(text_content)
else:
    print(f"Error:Unable to fetch content.Status code : {response.status_code}")
